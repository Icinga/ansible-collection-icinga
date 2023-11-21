# Role icinga.icinga.icingaweb2

The role icingaweb2 installs and configures Icinga Web 2 and its modules.

### Modules
* [Director](./module-director.md)
* [IcingaDB](./module-icingadb.md)
* [Monitoring](./module-monitoring.md)

## Databases

Icingaweb2 and some of its modules rely on a relational database to persist data. These databases **won't** be created by this role - you need to deploy and configure them in advance. For more information, see the [Databases](../getting-started.md#databases) section in the getting started guide.

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
