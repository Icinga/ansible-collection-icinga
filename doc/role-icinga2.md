# Role icinga.icinga.icinga2

The collection provides several roles to install and configure Icinga 2. This

## Variables

* `icinga2_purge_features: boolean`
  * Decides whether the unmanaged features should be purged or not. Default: true

* `icinga2_constants: dict`
  * Define constants in **constants.conf**, for defaults check the vars folder. 

```
icinga2_constants:
  NodeName: satellite.localdomain
  ZoneName: zone-satellite-d1
```

### Manage Configuration

If the local **conf.d** directory shouldn't be recursively included then the
var `icinga2_confd` should be set to `false`.

Otherwise you can use a directory name to set the include to a different folder
than **conf.d**. The folder needs to exist below /etc/icinga2. If it should be created by the role use the variable `icinga2_config_directories` in addition.

```
icinga2_confd: true/false/<directory_name>
```

### SELinux handling

The Icinga 2 role will automatically detect via Ansible facts if SELinux is enabled on the system. If this is the case the package icinga2-selinux will be automatically installed. 

If the package should be installed, even if SELinux is not enabled or somehow wrongly disabled in Ansible use the following variable. 

```
ansible_selinux:
  status: enabled
```