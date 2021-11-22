# Monitoring Objects Configuration

## Objects

By adding the variable `icinga2_objects` the role Icinga 2 will
generate configuration files with objects included.

This variable consists of Icinga 2 object attributes and attributes refering to the file created in the processs.

The second level of the dictionary tells on which host the configuration is created. All objects in the example below, will be created on the given host.: `host.example.org`.

The `file` key will be used to control in which directory structure the object will be placed.
In addition the `order` key will decide the order of the objects which are part of the file.
The default for `order` is set to 10, so everything below that number will be in front of the file, all objects with the order above 10 will be placed later in the file.

The `type` will be the original Icinga 2 object types, a list of all can be found in the documentation. [Icinga 2 Monitoring Objects](https://icinga.com/docs/icinga-2/latest/doc/09-object-types/#monitoring-objects)

```
icinga2_objects:
  host.example.org:
    - name: "{{ ansible_fqdn }}"
      type: Endpoint
      file: "{{ 'conf.d/' + ansible_hostname + '.conf' }}"
      order: 20
    - name: "{{ ansible_fqdn }}"
      type: Zone
      file: "{{ 'conf.d/' + ansible_hostname + '.conf' }}"
      order: 20
      endpoints:
        - "{{ ansible_fqdn }}"
      parent: main
```

More Examples at the end -> [Examples](#examples)

## Managing Config directories

To create or prepare the directories for the monitoring configuration use the variable `icinga2_config_directories`.
Those directories are only managed when they are part of `zones.d`, `conf.d` or the variable `icinga2_confd`.

```
icinga2_config_directories:
  - zones.d/main/hosts/
  - zones.d/main/services/
  - conf.d/commands/
```

## Parser Rules 

The collection provides the possibility to deploy Icinga 2 configuration, this includes configuration to shape the instance and monitoring data to create a complete monitoring environment. 

### Basic Syntax

The parser takes every value in the configuration and decides how the value should be written in the configuration. This takes a few rules to handle the configuration the right way.

First of all, to disable the parser use the prefix `-:`.

```
attr: -:"unparsed quoted string"
```

Strings are parsed in chunks, by splitting the original string into separate substrings at specific keywords (operators) such as `+`, `-`, `in`, `&&`, `||`, etc.

**NOTICE:** This splitting only works for keywords that are surrounded by whitespace, e.g.:

```
attr: string1 + string2 - string3
```

The algorithm will loop over the parameter and start by splitting it into 'string1' and 'string2 - string3'. 'string1' will be passed to the sub function 'value_types' and then the algorithm will continue parsing the rest of the string ('string2 - string3'), splitting it, passing it to value_types, etc.

Brackets are parsed for expressions:

```
attr: 3 * (value1 -  value2) / 2
```

The parser also detects function calls and will parse all parameters separately.

```
attr: function(param1, param2, ...)
```

Boolean values can be defined with or without quotes. In addition the Ansible bool types `yes` or `no` can be used either. 

```
attr: true or attr: 'true'
```

To avoid overlapping syntax with Ansible variable syntax, please refer to single quotes `' '` when using own lambda functions in Icinga. 

```
attrs => '{{ ... }}'
```

In general all values can be defined without quotes except for lamba functions where Ansible's own syntax would interfere with the double brackets.

| Type           | Examples                                 |
|----------------|------------------------------------------|
| Boolean        | `true`,`false`,`True`,`False`,`yes`,`no` |
| Numbers        | `2` or `3.5`                             |
| Time Intervals | `3m` or `3.5h`                           |
| String         | `attr: string`                           |

### Advanced Syntax

To replicate Icinga 2 advanced syntax like assignments with `+=` or `-=` you can use the prefix `+` or `-`.

To create the following Icinga 2 DSL syntax, 
```
var += config
```
simply use a string with the prefix `+` e.g. 

```
var: `+ config`
```

Because of the blank between the `+` and `config` those values are separately parsed and therefore numbers are also possible. For numbers we also can build `-=`, just use the minus sign `-`. This method will work for every attribute or custom attribute. 

```
attr: + -14 or attr: - -14
```

The parser is able to merge or reduce an array. For this method set the first item of your array as `+` or `-` sign. 

```
attr:
  - +
  - item1
  - item2 

# Alterntive syntax
attr: ['-','item1','item2']
```
Result in Icinga will be `attr += [ "item1", "item2", ]`.

To reduce arrays use the minus sign `-`. 

**NOTICE** Please be aware that the minus sign needs to be quoted otherwise the Ansible parser will have troubles reading the array.

```
attr: 
  - '-'
  - item1
  - item2

# Alterntive syntax
attr: ['-','item1','item2']
```

Result in Icinga will be `attr -= [ "item1", "item2", ]`.

#### Dictionaries

To merge dictionaries we can use the plus sign `+`. The plus sign needs to be a key in the dictionary. See following example.

```
attr: 
  +: true
  key1: value1 
```

The result:

```
attr["key1"] = "value1"
```

The useage of levels in dictionaries aren't limited. 

```
attr:
  key1:
    key2:
      key3:
        +: true
        value: test
```

Result: 

```
vars.attr["key1"] = {
    key2 = {
      key3 += {
        value = "test"
      }
    }
  }
```

### Examples:

#### Host

```
icinga2_objects:
  host.example.org:
    - name: agent.example.org
      type: Host
      file: zones.d/main/hosts.conf
      imports:
        - generic-host
      groups:
        - linux-hosts
      address: 192.168.2.10
      vars:
        os: linux

```

#### Host Group

```
icinga2_objects:
[...]
    - name: linux-host
      type: HostGroup
      file: zones.d/main/hostgroups.conf
      display_name: Linux Server
      assign:
        - host.vars.os == Linux
```

#### Service Apply

```
icinga2_objects:
[...]
  - name: ping
    type: Service
    order: 11
    file: zones.d/main/services.conf
    apply: true
    imports:
      - generic-service
    check_command: ping4
    assign:
      - host.address
```

#### Service Apply for 

```
[...]
  - name: ping
    type: Service
    apply: true
    apply_for: config in host.vars.ips
    check_command: ping4
    vars: + config
```

#### Service Object

```
icinga2_objects:
[...]
  - name: ping6
    type: Service
    file: zones.d/main/agent.localdomain.conf
    imports:
      - generic-service
    check_command: ping6
    host_name: agent.localdomain
```

#### Service Group

```
icinga2_objects:
[...]
  - name: service_group_linux
    type: ServiceGroup
    file: "local.d/groups.conf"
    display_name: Linux Services
    assign:
      - host.vars.os == linux
```

#### ApiUser

```
icinga2_objects:
[...]
  - name: icinga-api
    type: ApiUser
    file: "local.d/apiuser.conf"
    password: supersecrectpassword123
    permissions:
      - "objects/query/Host"
      - "objects/query/Service"

```

#### TimePeriod

```
icinga2_objects:
[...]
- name: 24x7
  type: TimePeriod
  file: "local.d/timeperiods.conf"
  ranges:
    monday: "00:00-24:00"
    tuesday: "00:00-24:00"
    wednesday: "00:00-24:00"
    thursday: "00:00-24:00"
    friday: "00:00-24:00"
```

#### Endpoint

```
icinga2_objects:
[...]
  - name: agent.localdomain
    type: Endpoint
    file: zones.d/main/hosts/agent.localdomain
    host: 10.10.10.10
```

#### Zone

```
icinga2_objects:
[...]
  - name: agent.localdomain
    type: Zone
    file: zones.d/main/hosts/agent.localdomain
    endpoints:
      - agent.localdomain
```

#### UserGroup

```
[...]
  - name: administrators
    type: UserGroup
    display_name: Admins
    file: zones.d/main/groups.conf
```



#### CheckCommand

```
icinga2_objects:
[...]
  - name: http
    command: [ PluginDir + /check_http ]
    type: CheckCommand
    file: zones.d/main/check_command.conf
    arguments:
      -H: $http_vhost$
      -S:
        set_if: $http_ssl$
```
