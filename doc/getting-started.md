### Getting Started

The collection includes two roles in the current version.

* icinga.repos: Role to manage repositories
* icinga.icinga2: Role to install and manage Icinga 2 instances.


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
ansible-galaxy collection install git+https://github.com/Icinga/ansible-collection-icinga.git,v0.1.0
```

Pre 2.10 you can also clone the repository, manually build and install the collection.

```
git clone https://github.com/Icinga/ansible-collection-icinga.git
ansible-galaxy collection build ansible-collection-icinga
ansible-galaxy collection install icinga-icinga-0.1.0.tar.gz
```
