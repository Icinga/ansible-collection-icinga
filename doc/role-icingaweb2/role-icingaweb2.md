# Role icinga.icinga.icingaweb2

The role icingaweb2 installs and configures Icinga Web 2 and its modules.

### Modules
* [Director](./module-director.md)
* [IcingaDB](./module-icingadb.md)
* [Monitoring](./module-monitoring.md)

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
