# Role icinga.icinga.icingaweb2

The role icingaweb2 installs and configures Icinga Web 2 and its modules.

### Modules
* [Director](./module-director.md)
* [IcingaDB](./module-icingadb.md)
* [Monitoring](./module-monitoring.md)

Custom modules can either be installed via package or git repository.
Therefore set the variable `source` with either `package` or a string consisting `git,repository_url,tag/version/branch` 
If no `tag/version/branch` is set the default `HEAD` will be used.

Furthermore it's possible to differentiate between your own custom modules (for example custom themes) and Icinga specific modules.

If you want to manage the config by yourself or the module doesn't need further configuration set the variable `manage_config` to `true` otherwise it needs to be set to `false`

Example:
```
icingaweb2_modules:
  my_theme:
    enabled: true
    manage_config: true
    source: git,https://github.com/slalomsk8er/icingaweb2-theme-solarized.git,v1.0.0
```

## Variables

### Icinga Web 2 DB Configuration

If you use this configuration it will be your main Icinga Web DB, this means if the variable `icingaweb2_db_import_schema` is used the schema will be imported to this database.

```
icingaweb2_db:
  type: mysql
  name: icingaweb
  host: 127.0.0.1
  user: icingaweb
  password: icingaweb
```

* `icingaweb2_db_import_schema: boolean`
  * Decides whether the schema should be imported in the database defined at `icingaweb2_db`. **Default: False**

* `icingaweb2_admin_<username|password>: string`
  * Set the username and password for the first admin user for Icinga Web 2.

#### Resources

Besides the standard Icinga Web 2 database you may configure additional resources for IcingaDB or automated imports.

```
icingaweb2_resources:
  icinga_ido:
    type: db
    db: mysql
    host: localhost
    dbname: icinga
    username: icinga
    password: icinga
    use_ssl: 0
    charset: utf8
  my_ldap:
    type: ldap
    [...]
```


