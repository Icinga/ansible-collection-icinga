# Feature API



```
icinga2_features:
  - name: api
    ssl_ca: /data/ca.crt
    ssl_cert: /opt/icinga/certproxy/current/certificate.pem
    ssl_key: /opt/icinga/certproxy/current/private_key.pem
    force_newcert: false
    endpoints:
      - name: NodeName
    zones:
      - name: ZoneName
        endpoints:
          - NodeName
```
