# Role icinga.icinga.icingadb

This role installs and configures the IcingaDB daemon. In addition it can also import the schema into the database. It is idempotent and works in HA-setups (two Icinga2 instances).

It serves as the official, more performant successor to Icinga IDO. More information about its purpose and design can be found [in the official documentation](https://icinga.com/docs/icinga-db/latest/doc/01-About/).


> :information_source: In many scenarios you want to install the [icingadb_redis role](../role-icingadb_redis/) together with this role. It is part of this collection, too.

## Variables

The following variables define the configuration for IcingaDB. Some variables got predefined [defaults](../../roles/icingadb/defaults/main.yml), others are purely opt-in.

For more information on the respective settings please see [the official documentation](https://icinga.com/docs/icinga-db/latest/doc/03-Configuration/).

### Database Configuration

| Variable | Type | Description | Default |
|----------|------|-------------|---------|
| `icingadb_database_ca` | `String` | Defines the path to the certificate authority for the TLS connection. | **n/a** |
| `icingadb_database_cert` | `String` | Defines the path to the certificate for client key authentication. | **n/a** |
| `icingadb_database_host` | `String` | Defines database address to connect to. | `127.0.0.1` |
| `icingadb_database_import_schema` | `bool` | Defines whether to import the schema into the database or not. | `false` |
| `icingadb_database_key` | `String` | Defines the path to the certificate key for client key authentication. | **n/a** |
| `icingadb_database_name` | `String` | Defines the database to connect to. | `icingadb` |
| `icingadb_database_password` | `String` | Defines the database password to connect with. | `icingadb` |
| `icingadb_database_port` | `int` | Defines the database port to connect to. | `3306` |
| `icingadb_database_tls` | `bool` | Defines whether to use TLS for the IcingaDB connection or not. | **n/a** |
| `icingadb_database_tls_insecure` | `bool` | Defines whether to skip TLS verification or not. | **n/a** |
| `icingadb_database_type` | `mysql\|pgsql` | Defines database type set in `icingadb.conf`. |  `mysql` |
| `icingadb_database_user` | `String` | Defines database user set in `icingadb.conf`. | `icingadb` |

### Redis configuration

| Variable | Type | Description | Default |
|----------|------|-------------|---------|
| `icingadb_redis_ca` | `String` | Defines the path to the certificate authority for the TLS connection. | **n/a** |
| `icingadb_redis_cert` | `String` | Defines the path to the certificate for client key authentication. | **n/a** |
| `icingadb_redis_host` | `String` | Defines database address to connect to. | `127.0.0.1` |
| `icingadb_redis_key` | `String` | Defines the path to the certificate key for client key authentication. | **n/a** |
| `icingadb_redis_password` | `String` | Defines the database password to connect with. | **n/a** |
| `icingadb_redis_port` | `int` | Defines the database port to connect to. | `6380` |
| `icingadb_redis_tls` | `bool` | Defines whether to use TLS for the IcingaDB connection or not. | **n/a** |
| `icingadb_redis_tls_insecure` | `bool` | Defines whether to skip TLS verification or not. | **n/a** |

### Logging configuration

For logging, currently only the **logging level** can be set. The default is `info`:

| Variable | Type | Description | Default |
|----------|------|-------------|---------|
| `icingadb_logging_level` | `fatal\|error\|warn\|info\|debug` | Defines the logging level for IcingaDB. | `info` |

### Miscellaneous

The following variables are used for the IcingaDB setup and are not directly related to the configuration of IcingaDB itself. Normally, you can rely on the defaults to work and should **not** change them unless you know what you are doing.

| Variable | Type | Description | Default |
|----------|------|-------------|---------|
| `icingadb_config_dir` | `String` | Defines the directory where the IcingaDB configuration is stored. | `/etc/icingadb` |
| `icingadb_database_schema` | `String` | Defines the path to the schema file. | `/usr/share/icingadb/schema/mysql.sql` |
| `icingadb_group` | `String` | Defines the group membership for the IcingaDB user. | `icingadb` |
| `icingadb_packages` | `List` | Defines the packages to install for IcingaDB. | `[icingadb]` |
| `icingadb_service_name` | `String` | Defines the name of the IcingaDB service. | `icingadb` |
| `icingadb_user` | `String` | Defines the user for the IcingaDB service. | `icingadb` |


## Examples

This play installs IcingaDB with on the same host as its connected MysQL database and redis instance. It also imports the schema into the database.

```yaml
- name: Install IcingaDB
  hosts: icingadb
  become: true
  vars:
    icingadb_database_import_schema: true  # Import the schema into the database

  roles:
    - role: icinga.icinga.icingadb
```

This more complex example installs IcingaDB and connects it to a **remote** PostgreSQL database, using client certificates and TLS. It also imports the schema into the database. Redis is installed locally.

```yaml
- name: Install IcingaDB
  hosts: icingadb
  become: true
  vars:
    icingadb_database_type: pgsql
    icingadb_database_host: postgresql.example.com
    icingadb_database_port: 5432
    icingadb_database_user: pg-icingadb
    icingadb_database_password: helloworld$123
    icingadb_database_tls: true
    icingadb_database_cert: /etc/icingadb/icingadb.crt
    icingadb_database_key: /etc/icingadb/icingadb.key
    icingadb_database_import_schema: true

  roles:
    - role: icinga.icinga.icingadb
```