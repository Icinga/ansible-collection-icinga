# Role icinga.icinga.icingadb

This role installs and configures the IcingaDB. In addition it can also import the schema into the database.


### Variables

Many variables are predefined by Icinga to make the installation easier. These are the main variables you could change.
Please consult the **icingadb_redis/defaults/main.yml** for all redis specific variables.

* `icingadb_redis_binds: list`
     * Defines redis server listener, default: ["127.0.0.1","::1"]

* `icingadb_redis_port: string`
     * Defines redis server port, default: 6380

### Manage Database Schema

If the role should automatically import the Icinga DB schema, you can set the following
variable. Please make sure the configured IcingaDB user is allowed to import at database level.

`icingadb_database_import_schema: false`
