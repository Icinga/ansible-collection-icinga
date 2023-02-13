# ansible-collection-icinga

[![CI](https://github.com/Icinga/ansible-collection-icinga/workflows/Build/badge.svg?event=push)](https://github.com/Icinga/ansible-collection-icinga/actions/workflows/build.yml/badge.svg)
[![PythonUnit](https://github.com/Icinga/ansible-collection-icinga/workflows/Python%20Unittest/badge.svg?event=push)](https://github.com/Icinga/ansible-collection-icinga/actions/workflows/python-test.yml/badge.svg)

Collection to setup and manage components of the Icinga software stack.

## Documentation and Roles
* [Getting Started](doc/getting-started.md)
* [Role: icinga.icinga.repos](doc/role-repos/role-repos.md)
* [Role: icinga.icinga.icinga2](doc/role-icinga2/role-icinga2.md)
  * [Parser and Monitoring Objects](doc/role-icinga2/objects.md)
  * [Features](doc/role-icinga2/features.md)
* [Role: icinga.icinga.monitoring_plugins](doc/role-monitoring_plugins/role-monitoring_plugins.md)
  * [List of Available Check Commands](check_command_list.md)

## Installation

You can easily install the collection with the `ansible-galaxy` command.

```
ansible-galaxy collection install icinga.icinga
```

Or if you are using Tower or AWX add the collection to your requirements file.

```
collections:
  - name: icinga.icinga
```

## Usage

To use the collection in your playbooks, add the collection and then use the roles.

```
- hosts: icinga-server
  roles:
    - icinga.icinga.repos
    - icinga.icinga.icinga2
    - icinga.icinga.monitoring_plugins
```
