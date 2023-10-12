## Module x509

### Variables and Configuration

The general module parameter like `enabled` and `source` can be applied here.

| Variable | Value      |
|----------|------------|
| enabled  | true/false |
| source   | package    |

#### Section configuration

The backend database for the module needs to be available and configured at the `icingaweb2_resources` variable.

```
icingaweb2_modules:
  x509:
    source: package
    enabled: true
    config:
      backend:
        resource: x509
```

#### Configure SNI Names.

To configure SNIs for a IP address, use the dictionary `sni`.

Example:

```
icingaweb2_modules:
  x509:
    source: package
    enabled: true
    config:
      backend:
        resource: x509
    sni:
      192.168.56.213:
        hostnames:
          - icinga.com
          - test2.icinga.com
```

#### Import Certificates

To import certificates use the **list** `certificate_files` all files need to be
available locally beforehand. 

```
icingaweb2_modules:
  x509:
    source: package
    enabled: true
    config:
      backend:
        resource: x509
    certificate_files:
      - /etc/ssl/certs/ca-certificates.crt
```
