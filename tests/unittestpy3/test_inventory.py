#!/usr/bin/python3

import sys
sys.path.insert(0,'plugins/inventory')

import unittest
from unittest.mock import patch, Mock, MagicMock, call

import requests
from requests.exceptions import SSLError, RequestException
from ansible.parsing.yaml.objects import AnsibleSequence, AnsibleMapping


from icinga import InventoryModule


class TestInventoryPlugin(unittest.TestCase):

    def test_get_recursive_sub_element(self):
        test_module = InventoryModule()
        test_dict   = {
                        "vars": {
                          "base_test": None,
                          "base test": None,
                          "index_test": [ { "test": True }, { "test": False } ],
                          "numeric_key": { "0": "zero" },
                          "ansible_vars": {
                            "ansible_user": "ansible1",
                            "ansible user": {
                              "name": "ansible2",
                            },
                          },
                          "ansible vars": {
                            "ansible_user": "ansible3",
                            "ansible user": {
                              "name": "ansible4",
                            },
                          },
                        },
                      }

        # Test cases that must succeed
        test_cases = [
                       ( 'vars.base_test', None ),
                       ( 'vars["base_test"]', None ),
                       ( 'vars[base_test]', None ),
                       ( 'vars.[base_test]', None ),
                       ( 'vars...[base_test]', None ),
                       ( 'vars...base_test', None ),

                       ( 'vars.base test', None ),
                       ( 'vars["base test"]', None ),
                       ( 'vars[base test]', None ),
                       ( 'vars.[base test]', None ),
                       ( 'vars...[base test]', None ),
                       ( 'vars...base test', None ),

                       ( 'vars.index_test[0].test', True ),
                       ( 'vars.index_test[1].test', False ),
                       ( 'vars.numeric_key["0"]', 'zero' ),

                       ( 'vars.ansible_vars.ansible_user', 'ansible1' ),
                       ( 'vars["ansible_vars"]["ansible_user"]', 'ansible1' ),
                       ( 'vars.ansible_vars["ansible_user"]', 'ansible1' ),
                       ( 'vars.["ansible_vars"].ansible_user', 'ansible1' ),

                       ( 'vars.ansible_vars.ansible user.name', 'ansible2' ),
                       ( 'vars.ansible_vars.["ansible user"].name', 'ansible2' ),

                       ( 'vars.ansible vars.ansible_user', 'ansible3' ),
                       ( 'vars.["ansible vars"].ansible_user', 'ansible3' ),
                       ( 'vars.[ansible vars].ansible_user', 'ansible3' ),

                       ( 'vars.ansible vars.ansible user.name', 'ansible4' ),
                       ( 'vars.["ansible vars"].ansible user.name', 'ansible4' ),
                       ( 'vars.[ansible vars].[ansible user].name', 'ansible4' ),

                       ( 'vars.ansible vars.ansible user', { "name": "ansible4" } ),
                     ]

        for search_string, expected in test_cases:
            self.assertEqual(test_module._get_recursive_sub_element(test_dict, search_string), expected)

        # Test cases that must throw exceptions
        fail_cases = [
                       'vars.bad_key',
                       'vars.index_test["0"].test',
                       'vars.numeric_key[0]',
                       'vars.index_test[100]',
                     ]

        for search_string in fail_cases:
            with self.assertRaises((IndexError, KeyError, TypeError)) as context:
                test_module._get_recursive_sub_element(test_dict, search_string)


    @patch('icinga.InventoryModule')
    def test_filter_key_validity(self, mock_init):
        # Test with known good filters
        mock_init.filters = {
                              "name": None,
                              "group": None,
                              "zone": None,
                              "custom": None,
                              "vars": {
                                "match": None,
                                "in": None,
                              },
                            }

        expected = True
        actual   = InventoryModule._validate_filter(mock_init)
        self.assertEqual(expected, actual)

        # Test with bad keys
        mock_init.filters = {
                              "bad_key": None,
                            }

        with self.assertRaises(Exception) as context:
            InventoryModule._validate_filter(mock_init)

        # Test with None filters key
        mock_init.filters = None
        expected = False
        actual   = InventoryModule._validate_filter(mock_init)
        self.assertEqual(expected, actual)


    @patch('icinga.InventoryModule')
    def test_filter_vars_keys_validty(self, mock_init):
        # Test with known good keys
        mock_init.filters = {
                              "vars": {
                                "match": None,
                                "in": None,
                              },
                            }

        expected = True
        actual   = InventoryModule._validate_filter(mock_init)
        self.assertEqual(expected, actual)

        # Test with bad keys
        mock_init.filters = {
                              "vars": {
                                "bad_key": None,
                              }
                            }

        with self.assertRaises(Exception) as context:
            InventoryModule._validate_filter(mock_init)


    @patch('icinga.InventoryModule')
    def test_api_url_validity(self, mock_init):
        valid_urls   = [
                         'http://localhost:5665/v1',
                         'https://localhost:5665/v1',
                         'https://localhost/v1',
                         'https://127.0.0.1:5665/v1',
                         'https://127.0.0.1/v1',
                         'https://[::1]:5665/v1',
                         'https://[::1]/v1',
                       ]
        invalid_urls = [
                         'https://localhost:5665',
                         'localhost:5665/v1',
                         'https://[::1]/',
                         '[::1]/v1',
                         'https:///v1',
                         'https://',
                       ]

        expected = True
        for url in valid_urls:
            actual = InventoryModule._validate_url(mock_init, url)
            self.assertEqual(expected, actual)

        expected = False
        for url in invalid_urls:
            actual = InventoryModule._validate_url(mock_init, url)
            self.assertEqual(expected, actual)


    def test_create_is_filter(self):
        items = [
                  ( 'test_variable', ['True'], '(host.test_variable==true)' ),
                  ( 'test_variable', ['true'], '(host.test_variable==true)' ),

                  ( 'test_variable', ['False'], '(host.test_variable==false)' ),
                  ( 'test_variable', ['false'], '(host.test_variable==false)' ),

                  ( 'test_variable', ['set'], '(host.test_variable)' ),
                  ( 'test_variable', ['SET'], '(host.test_variable)' ),

                  ( 'test_variable', ['!set'], '!(host.test_variable)' ),
                  ( 'test_variable', ['!SET'], '!(host.test_variable)' ),

                  ( 'test_variable', ['Null'], '(host.test_variable==null)' ),
                  ( 'test_variable', ['null'], '(host.test_variable==null)' ),

                  ( 'test_variable', ['None'], '(host.test_variable==null)' ),
                  ( 'test_variable', ['none'], '(host.test_variable==null)' ),

                  ( 'test_variable', ['!Null'], '!(host.test_variable==null)' ),
                  ( 'test_variable', ['!null'], '!(host.test_variable==null)' ),

                  ( 'test_variable', ['!None'], '!(host.test_variable==null)' ),
                  ( 'test_variable', ['!none'], '!(host.test_variable==null)' ),

                  ( 'test_variable', [ '!set', 'True', 'False', 'set'], '!(host.test_variable)' ),
                ]

        test_module = InventoryModule()

        for key, value, expected in items:
            actual = test_module._create_is_filter(key, value)
            self.assertEqual(expected, actual)

        # Expected Exception
        invalid_item = ( 'test_variable', ['anything_else'] )
        with self.assertRaises(ValueError) as context:
            test_module._create_is_filter(invalid_item[0], invalid_item[1])


    def test_create_in_filter(self):
        items = [
                  ( 'groups', [
                                'group1',
                              ],
                    r'((\"group1\" in host.groups))'
                  ),
                  ( 'groups', [
                                'group1',
                                'group2',
                              ],
                    r'((\"group1\" in host.groups)||(\"group2\" in host.groups))'
                  ),
                  ( 'groups', [
                                '!group1',
                              ],
                    r'(!(\"group1\" in host.groups))'
                  ),
                  ( 'groups', [
                                '!group1',
                                'group2',
                              ],
                    r'((\"group2\" in host.groups))&&(!(\"group1\" in host.groups))'
                  ),
                  ( 'groups', [
                                '!group1',
                                'group2',
                                '!group3',
                                'group4',
                              ],
                    r'((\"group2\" in host.groups)||(\"group4\" in host.groups))&&(!(\"group1\" in host.groups)&&!(\"group3\" in host.groups))'
                  ),
                ]

        test_module = InventoryModule()

        for key, values, expected in items:
            actual = test_module._create_in_filter(key, values)
            self.assertEqual(expected, actual)


    def test_create_match_filter(self):
        items = [
                  ( 'zone', [
                                'zone1',
                              ],
                    r'(match(\"zone1\", host.zone))'
                  ),
                  ( 'zone', [
                                'zone1',
                                'zone2',
                              ],
                    r'(match(\"zone1\", host.zone)||match(\"zone2\", host.zone))'
                  ),
                  ( 'zone', [
                                '!zone1',
                              ],
                    r'(!match(\"zone1\", host.zone))'
                  ),
                  ( 'zone', [
                                '!zone1',
                                'zone2',
                              ],
                    r'(match(\"zone2\", host.zone))&&(!match(\"zone1\", host.zone))'
                  ),
                  ( 'zone', [
                                '!zone1',
                                'zone2',
                                '!zone3',
                                'zone4',
                              ],
                    r'(match(\"zone2\", host.zone)||match(\"zone4\", host.zone))&&(!match(\"zone1\", host.zone)&&!match(\"zone3\", host.zone))'
                  ),
                ]

        test_module = InventoryModule()

        for key, values, expected in items:
            actual = test_module._create_match_filter(key, values)
            self.assertEqual(expected, actual)


    def test_create_filter(self):
        self.maxDiff = None
        test_module = InventoryModule()
        # Cannot pass an AnsibleMapping right now
        test_module.filters = {
                                "name": "satellite",
                                "group": AnsibleSequence([ "testgroup1", "testgroup2" ]),
                                "zone": AnsibleSequence([ "zone1", "zone2", "yetanotherzone" ]),
                                "custom": AnsibleSequence([ 'match(\\"some_custom_filter\\", host.name)' ]),
                                "vars": AnsibleMapping({ "match": { "operating_system": "win*"}, "in": { "services": None }}),
                              }

        test_module._validate_filter = MagicMock(return_value=True)
        actual   = test_module._create_filter()
        expected = r'((match(\"satellite\", host.name)))&&(((\"testgroup1\" in host.groups)||(\"testgroup2\" in host.groups)))&&((match(\"zone1\", host.zone)||match(\"zone2\", host.zone)||match(\"yetanotherzone\", host.zone)))&&(match(\"some_custom_filter\", host.name))&&((match(\"some_custom_filter\", host.name)))&&((match(\"win*\", host.vars.operating_system)))'
        self.assertEqual(expected, actual)

        # Test with empty return filter if given filter is invalid
        test_module._validate_filter = MagicMock(return_value=False)
        actual   = test_module._create_filter()
        expected = ''
        self.assertEqual(expected, actual)




    def test_populate_inventory(self):
        test_module = InventoryModule()
        test_module.inventory = MagicMock()
        test_module.inventory.add_host = MagicMock()
        test_module.inventory.add_group = MagicMock()
        test_module.inventory.set_variable = MagicMock()
        test_module._set_composite_vars = MagicMock()
        test_module._add_host_to_composed_groups = MagicMock()
        test_module._add_host_to_keyed_groups = MagicMock()
        test_module._add_host_to_composed_groups = MagicMock()

        # Set object attributes
        test_module.vars_prefix  = 'icinga_'
        test_module.want_ipv4    = True
        test_module.want_ipv6    = True
        test_module.ansible_user = 'vars.ansible_user'
        test_module.keyed_groups = [ { "prefix": "icinga_os", "key": "vars['operating_system']" } ]
        test_module.group_prefix = 'icinga_'
        test_module.compose      = None
        test_module.groups       = None
        test_module.strict       = False

        test_hosts = [
                       {
                         "name": "dummy_host1",
                         "attrs": {
                           "address": "127.0.0.1",
                           "address6": "",
                           "groups": [ "testgroup1", "testgroup2" ],
                           "zone": "master",
                         },
                       },
                       {
                         "name": "dummy_host2",
                         "attrs": {
                           "address": "",
                           "address6": "::1",
                           "command_endpoint": "",
                           "groups": [ "testgroup1", "testgroup3" ],
                           "templates": [ "dummy_host2", "Default Host" ],
                           "vars": {
                             "operating_system": "linux",
                             "distribution": "debian",
                             "ansible_user": "myansibleuser",
                           },
                           "zone": "satellite1",
                         },
                       },
                       {
                         "name": "dummy_host3",
                         "attrs": {
                           "address": "",
                           "address6": "",
                           "groups": [],
                           "zone": "anotherzone",
                         },
                       },
                     ]

        calls_add_group    = [
                               call('icinga_group_testgroup1'),
                               call('icinga_group_testgroup2'),
                               call('icinga_group_testgroup1'),
                               call('icinga_group_testgroup3'),
                             ]
        calls_add_host     = [
                               call('dummy_host1', 'icinga_group_testgroup1'),
                               call('dummy_host1', 'icinga_group_testgroup2'),
                               call('dummy_host2', 'icinga_group_testgroup1'),
                               call('dummy_host2', 'icinga_group_testgroup3'),
                               call('dummy_host3')
                             ]
        calls_set_variable = [
                               call('dummy_host1', 'icinga_address', '127.0.0.1'),
                               call('dummy_host1', 'icinga_address6', ''),
                               call('dummy_host1', 'icinga_groups', ['testgroup1', 'testgroup2']),
                               call('dummy_host1', 'icinga_zone', 'master'),
                               call('dummy_host1', 'ansible_host', '127.0.0.1'),
                               call('dummy_host2', 'icinga_address', ''),
                               call('dummy_host2', 'icinga_address6', '::1'),
                               call('dummy_host2', 'icinga_command_endpoint', ''),
                               call('dummy_host2', 'icinga_groups', ['testgroup1', 'testgroup3']),
                               call('dummy_host2', 'icinga_templates', ['dummy_host2', 'Default Host']),
                               call('dummy_host2', 'icinga_vars', {'operating_system': 'linux', 'distribution': 'debian', 'ansible_user': 'myansibleuser'}),
                               call('dummy_host2', 'icinga_zone', 'satellite1'),
                               call('dummy_host2', 'ansible_host', '::1'),
                               call('dummy_host2', 'ansible_user', 'myansibleuser'),
                               call('dummy_host3', 'icinga_address', ''),
                               call('dummy_host3', 'icinga_address6', ''),
                               call('dummy_host3', 'icinga_groups', []),
                               call('dummy_host3', 'icinga_zone', 'anotherzone'),
                             ]
        calls_composite    = [
                               call( None,
                                     { 'address': '127.0.0.1',
                                       'address6': '',
                                       'groups': ['testgroup1', 'testgroup2'],
                                       'zone': 'master'
                                     },
                                     'dummy_host1',
                                     strict=False
                                   ),
                               call( None,
                                     { 'address': '',
                                       'address6': '::1',
                                       'command_endpoint': '',
                                       'groups': ['testgroup1', 'testgroup3'],
                                       'templates': ['dummy_host2', 'Default Host'],
                                       'vars': {
                                         'operating_system': 'linux',
                                         'distribution': 'debian',
                                         'ansible_user': 'myansibleuser'
                                       },
                                       'zone': 'satellite1'
                                     },
                                     'dummy_host2',
                                     strict=False
                                   ),
                               call( None,
                                     { 'address': '',
                                       'address6': '',
                                       'groups': [],
                                       'zone': 'anotherzone',
                                     },
                                     'dummy_host3',
                                     strict=False,
                                   ),
                             ]
        calls_composed     = [
                               call( None,
                                     { 'address': '127.0.0.1',
                                       'address6': '',
                                       'groups': ['testgroup1', 'testgroup2'],
                                       'zone': 'master'
                                     },
                                     'dummy_host1',
                                     strict=False),
                               call( None,
                                     { 'address': '',
                                       'address6': '::1',
                                       'command_endpoint': '',
                                       'groups': ['testgroup1', 'testgroup3'],
                                       'templates': ['dummy_host2', 'Default Host'],
                                       'vars': {
                                         'operating_system': 'linux',
                                         'distribution': 'debian',
                                         'ansible_user': 'myansibleuser'
                                       },
                                       'zone': 'satellite1'
                                     },
                                     'dummy_host2',
                                     strict=False),
                               call( None,
                                     { 'address': '',
                                       'address6': '',
                                       'groups': [],
                                       'zone': 'anotherzone'
                                     },
                                     'dummy_host3',
                                     strict=False),
                             ]
        calls_keyed        = [
                               call([
                                     {'prefix': 'icinga_os',
                                      'key': "vars['operating_system']"},
                                     {'prefix': 'icinga_zone',
                                      'key': 'zone'}
                                    ],
                                    {'address': '127.0.0.1',
                                     'address6': '',
                                     'groups': ['testgroup1', 'testgroup2'],
                                     'zone': 'master'
                                    },
                                    'dummy_host1',
                                    strict=False
                                  ),
                               call([
                                     {'prefix': 'icinga_os',
                                      'key': "vars['operating_system']"},
                                     {'prefix': 'icinga_zone',
                                      'key': 'zone'}
                                    ],
                                    {'address': '',
                                     'address6': '::1',
                                     'command_endpoint': '',
                                     'groups': ['testgroup1', 'testgroup3'],
                                     'templates': ['dummy_host2', 'Default Host'],
                                     'vars': {
                                       'operating_system': 'linux',
                                       'distribution': 'debian',
                                       'ansible_user': 'myansibleuser'
                                     },
                                     'zone': 'satellite1'},
                                     'dummy_host2',
                                     strict=False),
                               call([
                                     {'prefix': 'icinga_os',
                                      'key': "vars['operating_system']"},
                                     {'prefix': 'icinga_zone',
                                      'key': 'zone'}
                                    ],
                                    {'address': '',
                                     'address6': '',
                                     'groups': [],
                                     'zone': 'anotherzone'},
                                     'dummy_host3',
                                     strict=False),
                             ]

        test_module._populate_inventory(test_hosts)
        # Assertions
        test_module.inventory.add_group.assert_has_calls(calls_add_group, any_order=False)
        test_module.inventory.add_host.assert_has_calls(calls_add_host, any_order=False)
        test_module.inventory.set_variable.assert_has_calls(calls_set_variable, any_order=False)
        test_module._set_composite_vars.assert_has_calls(calls_composite, any_order=False)
        test_module._add_host_to_composed_groups.assert_has_calls(calls_composed, any_order=False)
        test_module._add_host_to_keyed_groups.assert_has_calls(calls_keyed, any_order=False)


    @patch('icinga.InventoryModule')
    def test_get_hosts(self, mock_init):

        class mocked_get_session_good():
            def get(*args, **kwargs):
                return True
            def post(*args, **kwargs):
                m = Mock()
                m.status_code = 200
                m.json.return_value = { "results": [] }
                return m

        class mocked_get_session_sslerror():
            def get(*args, **kwargs):
                raise SSLError

        class mocked_get_session_requestexception():
            def get(*args, **kwargs):
                raise RequestException

        class mocked_get_session_bad_status_code():
            def get(*args, **kwargs):
                return True
            def post(*args, **kwargs):
                m = Mock()
                m.status_code = 404
                m.json.return_value = { "error": 404, "status": "No objects found." }
                return m

        # Should succeed and return hosts (empty list)
        mock_init._get_session.return_value = mocked_get_session_good()
        expected = list()
        actual   = InventoryModule._get_hosts(mock_init)
        self.assertEqual(actual, expected)

        # Should raise SSLError
        mock_init._get_session.return_value = mocked_get_session_sslerror()
        with self.assertRaises(SSLError) as context:
            InventoryModule._get_hosts(mock_init)

        # Should raise RequestException
        mock_init._get_session.return_value = mocked_get_session_requestexception()
        with self.assertRaises(RequestException) as context:
            InventoryModule._get_hosts(mock_init)

        # Should raise ValueError
        mock_init._get_session.return_value = mocked_get_session_bad_status_code()
        with self.assertRaises(ValueError) as context:
            InventoryModule._get_hosts(mock_init)
