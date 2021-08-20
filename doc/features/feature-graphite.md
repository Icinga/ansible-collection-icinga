## Graphite

To enable the feature Graphite use the following block in the variable `icinga2_features`.

```
icinga2_features:
  - name: graphite
    host: localhost
    port: 2003
```

### Feature variables

* `host: string`
  * Name or address of the graphite instance.

* `port: int`
  *  
