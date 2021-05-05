# Role icinga.icinga.icinga2

The collection provides several roles to install and configure Icinga 2. This

## Variables

### Mange Configuration

If the local **conf.d** directory shouldn't be recursively included then the
var `icinga2_confd` should be set to `false`.

Otherwise you can use a directory name to set the include to a different folder
than **conf.d**. The folder needs to exist below /etc/icinga2. If it should be created by the role use the variable `icinga2_config_directories` in addition.



```
icinga2_confd: true/false/<directory_name>

```
