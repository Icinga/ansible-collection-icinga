## Module Reporting

The module Reporting provides a way to generate reports based on data provided by Icinga2.

## Configuration

The general module parameter like `enabled` and `source` can be applied here.

Configuration is done via the `reporting` section of the `icingaweb2_modules` variable. In addition to the general module parameters `backend.resource` and `mail.from`, a **database connection** can be defined for automatically creating the required tables. in the referenced database resource.

Example:
```yaml
icingaweb2_modules:
  reporting:
    enabled: true
    source: git
    config:
      backend:
        resource: reporting-db
      mail:
        from: icinga@example.com
    database:
      import_schema: true
      host: localhost
      port: 3306
      user: reporting
      password: reporting
      type: mysql
```
