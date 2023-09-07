#!/usr/bin/python3

import sys
sys.path.insert(0,'plugins/inventory')

import unittest
from unittest.mock import patch, Mock

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
                     ]

        for search_string in fail_cases:
            with self.assertRaises((KeyError, TypeError)) as context:
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
