### Getting Started

The collection includes two roles in the current version.

* icinga.repos: Role to manage repositories
  * [Documentation: doc/role-repos](role-repos/role-repos.md)
* icinga.icinga2: Role to install and manage Icinga 2 instances.
  * [Documentation: doc/role-icinga2](role-icinga2/role-icinga2.md)


---
**NOTE**

Please be careful if you have an existing installation and you want to use the
collection. All features which are not configured will be disabled.

---

## Installation

To start with the collection, easily install it with the **ansible-galaxy** command.

Installation from Galaxy Server:

```
ansible-galaxy collection install icinga.icinga
```

Or pull the collection from the git. (Only useable with Ansible version 2.10.9)
```
ansible-galaxy collection install git+https://github.com/Icinga/ansible-collection-icinga.git,0.1.0
```

Pre 2.10 you can also clone the repository, manually build and install the collection.

```
git clone https://github.com/Icinga/ansible-collection-icinga.git
ansible-galaxy collection build ansible-collection-icinga
ansible-galaxy collection install icinga-icinga-0.1.0.tar.gz
```

## Example Playbooks

This is an example on how to install an Icinga 2 server/master instance.

```
- name: install icinga2 master
  hosts: master
  vars:
    icinga2_constants:  # Set default constants and TicketSalt for the CA
      TicketSalt: "{{ lookup('ansible.builtin.password', '.icinga-server-ticketsalt') }}"
      NodeName: "{{ ansible_fqdn }}"
      ZoneName: "main"
    icinga2_confd: false # Disable example configuration
    icinga2_purge_features: yes # Ansible will manage all features
    icinga2_config_directories:  # List of directories in which the role will manage monitoring objects
      - zones.d/main/commands
      - zones.d/main/hosts
      - zones.d/main/services
    icinga2_features:
      - name: api           # Enable Feature API
        ca_host: none       # No CA host, CA will be created locally
        endpoints:
          - name: NodeName
        zones:
          - name: ZoneName
            endpoints:
              - NodeName
      - name: checker
        state: present
      - name: notification
        state: present
      - name: idomysql
        state: present
        import_schema: false   # Enable this if the database and permissions for the user is created in advance.
        user: icinga
        password: icinga123
        database: icingaido
        cleanup:
          downtimehistory_age: 31d
          contactnotifications_age: 31d
      - name: mainlog
        severity: information

  roles:
    - icinga.icinga.repos
    - icinga.icinga.icinga2
```

This is an example on how to install an Icinga 2 agent instance.

```
- name: install icinga2 agent
  hosts: agent
  vars:
    icinga2_confd: false # Disable example configuration
    icinga2_purge_features: yes # Ansible will manage all features
    icinga2_features:
      - name: api           # Enable Feature API
        ca_host: master.localdomain      
        # Trusted Cert and Ticket will be gathered from this host.
        # Ticket will be "delegated" if the FQDN is not in your Ansible environment
        # use the variable icinga2_delegate_host in addition.
        endpoints:
          - name: NodeName
        zones:
          - name: ZoneName
            endpoints:
              - NodeName
      - name: notification
        state: absent

  roles:
    - icinga.icinga.repos
    - icinga.icinga.icinga2
```
