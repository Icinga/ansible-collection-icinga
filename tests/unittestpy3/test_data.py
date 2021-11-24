from plugins.module_utils.parse import Icinga2Parser
import unittest


class TestIcingaParser(unittest.TestCase):
    def test_true(self):
        ip = Icinga2Parser()
        data = {
            "test": "true"
        }
        constants = ["NodeName", "ZoneName"]
        result = ip.parse(attrs=data, constants=constants)
        #print("Tested boolean true: " + result)
        self.assertEqual(result, 'test = true\n')

    def test_false(self):
        ip = Icinga2Parser()
        data = {
            "test": "false"
        }
        constants = ["NodeName", "ZoneName"]
        result = ip.parse(attrs=data, constants=constants)
        #print("Tested boolean false: " + result)
        self.assertEqual(result, 'test = false\n')

    def test_string(self):
        ip = Icinga2Parser()
        data = {
            "test": "string"
        }
        constants = ["NodeName", "ZoneName"]
        result = ip.parse(attrs=data, constants=constants)
        #print("Tested string: " + result)
        self.assertEqual(result, 'test = "string"\n')

    def test_array(self):
        ip = Icinga2Parser()
        data = {
            "test": ["item1", "item2", "NodeName"]
        }
        constants = ["NodeName", "ZoneName"]
        result = ip.parse(attrs=data, constants=constants)
        #print("Tested array: " + result)
        self.assertEqual(result, 'test = [ "item1", "item2", NodeName, ]\n')

    def test_constants(self):
        ip = Icinga2Parser()
        data = {
            "test": "NodeName"
        }
        constants = ["NodeName", "ZoneName"]
        result = ip.parse(attrs=data, constants=constants)
        #print("Tested constants: " + result)
        self.assertEqual(result, 'test = NodeName\n')

    def test_dict(self):
        ip = Icinga2Parser()
        data = {
            "test": {
                "item1": "value1",
                "item2": "value2"
            }
        }
        constants = ["NodeName", "ZoneName"]
        result = ip.parse(attrs=data, constants=constants)
        #print("Tested dictionaries: " + result)
        self.assertMultiLineEqual(result, 'test = {\n  item1 = "value1"\n  item2 = "value2"\n}\n')

    def test_unparsed(self):
        ip = Icinga2Parser()
        data = {
            "test": '-:"test NodeName"',
        }
        constants = ["NodeName", "ZoneName"]
        result = ip.parse(attrs=data, constants=constants)
        #print("Tested Unparsed: " + result)
        self.assertMultiLineEqual(result, 'test = "test NodeName"\n')

    def test_function(self):
        ip = Icinga2Parser()
        data = {
            "test": 'match(*prod-sfo*, host.name)',
        }
        constants = ["NodeName", "ZoneName"]
        result = ip.parse(attrs=data, constants=constants)
        #print("Tested Functions: " + result)
        self.assertMultiLineEqual(result, 'test = match("*prod-sfo*", host.name)\n')

    def test_rocketsyntax_plus(self):
        ip = Icinga2Parser()
        data = {
            "test": "+ config",
        }
        constants = ["NodeName", "ZoneName", "config"]
        result = ip.parse(attrs=data, constants=constants)
        #print("Tested rocketsyntax plus: " + result)
        self.assertMultiLineEqual(result, 'test += config\n')

    def test_rocketsyntax_minus(self):
        ip = Icinga2Parser()
        data = {
            "test": "- string",
        }
        constants = ["NodeName", "ZoneName", "config"]
        result = ip.parse(attrs=data, constants=constants)
        #print("Tested rocketsyntax minus: " + result)
        self.assertMultiLineEqual(result, 'test -= "string"\n')

    def test_rocketsyntax_alt_plus(self):
        ip = Icinga2Parser()
        data = {
            "test": ["+", "item1", "ZoneName"],
        }
        constants = ["NodeName", "ZoneName", "config"]
        result = ip.parse(attrs=data, constants=constants)
        #print("Tested rocketsyntax alt plus: " + result)
        self.assertMultiLineEqual(result, 'test += [ "item1", ZoneName, ]\n')

    def test_rocketsyntax_alt_minus(self):
        ip = Icinga2Parser()
        data = {
            "test": ["-", "item1", "ZoneName"],
        }
        constants = ["NodeName", "ZoneName", "config"]
        result = ip.parse(attrs=data, constants=constants)
        #print("Tested rocketsyntax alt minus: " + result)
        self.assertMultiLineEqual(result, 'test -= [ "item1", ZoneName, ]\n')

    def test_rocketsyntax_merge_keys(self):
        ip = Icinga2Parser()
        data = {
            "vars": {
                "+": "true",
                "item1": "value1",
                "item2": "NodeName"
            },
        }
        constants = ["NodeName", "ZoneName", "config"]
        result = ip.parse(attrs=data, constants=constants)
        #print("Tested merge keys: " + result)
        self.assertMultiLineEqual(result, 'vars.item1 = "value1"\nvars.item2 = NodeName\n')

    def test_timeintervals(self):
        ip = Icinga2Parser()
        data = {
            "check_interval": "3m",
            "wrong_interval": "3f"
        }
        constants = ["NodeName", "ZoneName", "config"]
        result = ip.parse(attrs=data, constants=constants)
        #print("Tested timeintervals: " + result)
        self.assertMultiLineEqual(result, 'check_interval = 3m\nwrong_interval = "3f"\n')

    def test_numbers(self):
        ip = Icinga2Parser()
        data = {
            "num1": "3",
            "num2": "2.5"
        }
        constants = ["NodeName", "ZoneName", "config"]
        result = ip.parse(attrs=data, constants=constants)
        #print("Tested numbers: " + result)
        self.assertMultiLineEqual(result, 'num1 = 3\nnum2 = 2.5\n')

    def test_cust_func(self):
        ip = Icinga2Parser()
        data = {
            "func": "{{ function_blubber(param1,NodeName) }}"
        }
        constants = ["NodeName", "ZoneName", "config"]
        result = ip.parse(attrs=data, constants=constants)
        #print("Tested custom functions: " + result)
        self.assertMultiLineEqual(result, 'func = {{  function_blubber(param1,NodeName)  }}\n')

    def test_math(self):
        ip = Icinga2Parser()
        data = {
            "math_is_fun": "3 * (value1 -  value2) / 2"
        }
        constants = ["NodeName", "ZoneName", "config"]
        result = ip.parse(attrs=data, constants=constants)
        #print("Tested math: " + result)
        self.assertMultiLineEqual(result, 'math_is_fun = 3 * ("value1" -  "value2") / 2\n')

    def test_assign_rules(self):
        ip = Icinga2Parser()
        data = {
            "assign": ["match(hostname.fqdn.com, host.name)"]
        }
        constants = ["NodeName", "ZoneName", "config"]
        result = ip.parse(attrs=data, constants=constants)
        #print("Tested assign rule: " + result)
        self.assertMultiLineEqual(result, 'assign where match("hostname.fqdn.com", host.name)\n')

    def test_ignore_rules(self):
        ip = Icinga2Parser()
        data = {
            "ignore": ["match(hostname.fqdn.com, host.name)"]
        }
        constants = ["NodeName", "ZoneName", "config"]
        result = ip.parse(attrs=data, constants=constants)
        #print("Tested assign rule: " + result)
        self.assertMultiLineEqual(result, 'ignore where match("hostname.fqdn.com", host.name)\n')


if __name__ == '__main__':
    unittest.main()
