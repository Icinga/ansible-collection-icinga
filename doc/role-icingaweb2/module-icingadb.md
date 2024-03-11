## Module IcingaDB

This module IcingaDB is the replacement for the monitoring module with IcingaDB as database backend.

## Configuration

The general module parameter like `enabled` and `source` can be applied here.

For every config file, create a dictionary with sections as keys and the parameters as values. For all parameters please check the [module documentation](https://icinga.com/docs/icinga-db-web/latest/doc/01-About/)

```
icingaweb2_modules:
  icingadb:
    enabled: true
    source: package
    commandtransports:
      instance01:
        transport: api
        host: 127.0.0.1
        username: root
        password: root
    config:
      icingadb:
        resource: icingadb
      redis:
        tls: '0'
    redis:
      redis1:
        host: "192.168.56.200"
      redis2:
        host: "192.168.56.201"
```

As the parameter for the redis TLS connection aren't documented at the official docs. Please use the following parameters to configure TLS connections. At the redis section add the following:

```
redis:
  tls: '1'
  ca: /path/to/ca.crt
  cert: /path/to/cert.crt
  key: /path/to/key.key
```
