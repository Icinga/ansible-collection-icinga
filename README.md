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
* [Role: icinga.icinga.icingadb](doc/role-icingadb/role-icingadb.md)
* [Role: icinga.icinga.icingadb_redis](doc/role-icingadb_redis/role-icingadb_redis.md)
* [Role: icinga.icinga.icingaweb2](doc/role-icingaweb2/role-icingaweb2.md)
* [Role: icinga.icinga.monitoring_plugins](doc/role-monitoring_plugins/role-monitoring_plugins.md)
  * [List of Available Check Commands](doc/role-monitoring_plugins/check_command_list.md)
* [Inventory Plugin: icinga.icinga.icinga](doc/plugins/inventory/icinga-inventory-plugin.md)


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
    - icinga.icinga.icingadb
    - icinga.icinga.icingadb_redis
    - icinga.icinga.monitoring_plugins
```

## License

Copyright 2023 Icinga GmbH

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
