# ansible-collection-icinga

[![CI](https://github.com/Icinga/ansible-collection-icinga/workflows/CI/badge.svg?event=push)](https://github.com/Icinga/ansible-collection-icinga/actions?query=workflow%3ACI)

Collection to setup and manage components of the Icinga software stack.

## Roles

* [icinga.icinga.repos](doc/role-repos.md)
* [icinga.icinga.icinga2](doc/role-icinga2.md)
  * [Monitoring Objects](doc/objects.md)
  * [Features](doc/features.md)
    * [Feature API](doc/features/feature-api.md)
    * [Feature IDO](doc/features/feature-ido.md)


## Installation

You can easily install the collection with the `ansible-galaxy` command.

```
ansible-galaxy collection install git+https://github.com/Icinga/ansible-collection-icinga.git,v0.1.0
```

Or if you are using Tower or AWX add the collection to your requirements file.

```
collections:
  - name: https://github.com/Icinga/ansible-collection-icinga.git
    type: git
    version: v0.1.0
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
