# ansible-collection-icinga

[![CI](https://github.com/Icinga/ansible-collection-icinga/workflows/build/badge.svg?event=push)](https://github.com/Icinga/ansible-collection-icinga/actions/workflows/build.yml/badge.svg)
[![PythonUnit](https://github.com/Icinga/ansible-collection-icinga/workflows/Python%20Unittest/badge.svg?event=push)](https://github.com/Icinga/ansible-collection-icinga/actions/workflows/python-test.yml/badge.svg)

Collection to setup and manage components of the Icinga software stack.

## Documentation and Roles
* [Getting started](doc/getting-started.md)
* [Role: icinga.icinga.repos](doc/role-repos.md)
* [Role: icinga.icinga.icinga2](doc/role-icinga2.md)
  * [Parser and Monitoring Objects](doc/objects.md)
  * [Features](doc/features.md)
    * [Feature API](doc/features/feature-api.md)
    * [Feature IDO](doc/features/feature-ido.md)
    * [Feature mainlog](doc/features/feature-mainlog.md)
    * [Feature notification](doc/features/feature-notification.md)
    * [Feature InfluxDB](doc/features/feature-influxdb.md)
    * [Feature Graphite](doc/features/feature-graphite.md)


## Installation

You can easily install the collection with the `ansible-galaxy` command.

```
ansible-galaxy collection install git+https://github.com/Icinga/ansible-collection-icinga.git,0.1.0
```

Or if you are using Tower or AWX add the collection to your requirements file.

```
collections:
  - name: https://github.com/Icinga/ansible-collection-icinga.git
    type: git
    version: 0.1.0
```

## Usage

To use the collection in your playbooks, add the collections and then use the roles

```
- hosts: icinga-server
  collections:
    - icinga.icinga
  roles:
    - repos
    - icinga2
```
