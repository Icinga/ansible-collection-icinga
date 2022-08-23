# Icinga 2 Features

To configure features in addition to the set defaults use the variable `icinga2_features`.

Icinga 2 features can be added with their attributes as described in the Icinga 2 documentation.
[Documentation Icinga 2 Features](https://icinga.com/docs/icinga-2/latest/doc/09-object-types/#features)

A few other features can have more attributes to configure the feature itself, like the [API feature](features/feature-api.md).

Current supported features:

* [Feature API](features/feature-api.md)
* [Feature IDO](features/feature-ido.md)
* [Feature mainlog](features/feature-mainlog.md)
* [Feature notification](features/feature-notification.md)
* [Feature InfluxDB](features/feature-influxdb.md)
* [Feature Graphite](features/feature-graphite.md)

```
icinga2_features:
  - name: checker
  - name: mainlog
  - name: graphite
    host: localhost
    port: 3000
  - name: api
    force_newcert: false
    endpoints:
      - name: NodeName
    zones:
      - name: ZoneName
        endpoints:
          - NodeName
```
