## Feature IDO

The feature for the IDO connection installs, enables and configures the object and in
addition is able to import the db_schema. This is only possible if the mysql or
pgsql client binary is available.

If the database is available use the boolean key `import_schema` to enable
import schema.

All other keys are equal to the object type an can be found in the documentation.

* [IdoPgsqlConnection](https://icinga.com/docs/icinga-2/latest/doc/09-object-types/#idopgsqlconnection)
* [IdoMysqlConnection](https://icinga.com/docs/icinga-2/latest/doc/09-object-types/#idomysqlconnection)

#### Example MYSQL:

```
icinga2_features:
  - name: idomysql
    host: localhost
    port: 3306
    database: icinga2
    user: icinga2
    password: icinga2
    import_schema: false
    cleanup:
      downtimehistory: 48h
      contactnotifications_age: 31d
```

#### Example PGSQL:

```
icinga2_features:
  - name: idopgsql
    host: localhost
    database: icinga2
    user: icinga2
    password: icinga2
    import_schema: true
    cleanup:
      downtimehistory: 48h
      contactnotifications_age: 31d
```
