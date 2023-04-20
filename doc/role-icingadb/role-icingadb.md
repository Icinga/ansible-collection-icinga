# Role icinga.icinga.icingadb

This role installs and configures the IcingaDB. In addition it can also import the schema into the database.


### Variables

* `icingadb_database_type: string`
  * Defines which database type should be configured in the config file. Default: mysql

* `icingadb_database_host: string`
  * Defines the IcingaDB address at the config file. Default: 127.0.0.1

* `icingadb_database_port: string`
  * Defines database port at the icingadb.conf. Default: 3306

* `icingadb_database_name: string`
  * Defines database name at the icingadb.conf. Default: icingadb

* `icingadb_database_user: string`
  * Defines database user at the icingadb.conf. Default: icingadb

* `icingadb_database_password: string`
  * Defines database password at the icingadb.conf. Default: icingadb

* `icingadb_database_tls: boolean`
  * Defines wether to use TLS for the IcingaDB connection.

* `icingadb_database_cert: string`
  * Defines the path to the certificate for the tls connection.

* `icingadb_database_key: string`
  * Defines the path to the certificate key for the tls connection.





### Manage Database Schema

If the role should automatically import the Icinga DB schema, you can set the following
variable. Please make sure the configured IcingaDB user is allowed to import at database level.

`icingadb_database_import_schema: false`
