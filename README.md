# ansible-collection-icinga

[![CI](https://github.com/Icinga/ansible-collection-icinga/workflows/Build/badge.svg?event=push)](https://github.com/Icinga/ansible-collection-icinga/actions/workflows/build.yml/badge.svg)
[![PythonUnit](https://github.com/Icinga/ansible-collection-icinga/workflows/Python%20Unittest/badge.svg?event=push)](https://github.com/Icinga/ansible-collection-icinga/actions/workflows/python-test.yml/badge.svg)

Collection to setup and manage components of the Icinga software stack.

## Documentation and Roles
* [Getting started](doc/getting-started.md)
* [Role: icinga.icinga.repos](doc/role-repos.md)
* [Role: icinga.icinga.icinga2](doc/role-icinga2.md)
  * [Parser and Monitoring Objects](doc/objects.md)
  * [Features](doc/features.md)
    * [Feature API](doc/features/feature-api.md)
    * [Feature Command](doc/features/feature-command.md)
    * [Feature ElasticSearch](doc/features/feature-elasticsearch.md)
    * [Feature Graphite](doc/features/feature-graphite.md)
    * [Feature IcingaDB](doc/features/feature-icingadb.md)
    * [Feature IDO](doc/features/feature-ido.md)
    * [Feature InfluxDB](doc/features/feature-influxdb.md)
    * [Feature InfluxDB2](doc/features/feature-influxdb2.md)
    * [Feature mainlog](doc/features/feature-mainlog.md)
    * [Feature notification](doc/features/feature-notification.md)




## Installation

You can easily install the collection with the `ansible-galaxy` command.

```
ansible-galaxy collection install icinga.icinga
```

Or if you are using Tower or AWX add the collection to your requirements file.

```
collections:
  - name: icinga.icinga
    version: 0.1.0
```

## Usage

To use the collection in your playbooks, add the collection and then use the roles.

```
- hosts: icinga-server
  roles:
    - icinga.icinga.repos
    - icinga.icinga.icinga2
```
