# Icinga 2 Features

To configure features in addition to the set defaults us the variable `icinga2_features`.

```
icinga2_features:
  - name: checker
  - name: mainlog
  - name: api
    force_newcert: false
    endpoints:
      - name: NodeName
    zones:
      - name: ZoneName
        endpoints:
          - NodeName
```
