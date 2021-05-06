## Feature API

The API Feature configures the server or agent API. The feature will create
certificates, certificate signing requests and manage the **zones.conf**.

All attributes of the object type [ApiListener](https://icinga.com/docs/icinga-2/latest/doc/09-object-types/#apilistener) can be added as keys.

All non Icinga attributes to configure the feature are explained below.


```
icinga2_features:
  - name: api
    force_newcert: false
    ca_host: icinga-server.localdomain
    endpoints:
      - name: NodeName
    zones:
      - name: ZoneName
        endpoints:
          - NodeName
```

### Icinga Server

To create an Icinga 2 server the API should setup a *CA* this can be done with
the parameter `icinga2_ca_host`. Set it to **none** if the role should create
a CA on the server.

```
ca_host: none
```

### Icinga Agent

If the role should create certificates for your **client** and request them by the
satellite or server.
Set the variable `icinga2_ca_host` to the address or name of the parent.

```
ca_host: icinga-server.localdomain
```

If you want to use certificates which aren't created by **Icinga 2 CA**, then use
the following variables to point the role to your own certificates.

```
ssl_ca: /opt/icinga/ca.crt
ssl_cert: /opt/icinga/certificate.crt
ssl_key: /opt/icinga/certificate.key
```

The role tries to copy the certificates on the remote location to
**/var/lib/icinga2/certs** named after the value `cert_name`.

```
icinga2_features:
  - name: api
    ssl_ca: /opt/icinga/ca.crt
    ssl_cert: /opt/icinga/certificate.crt
    ssl_key: /opt/icinga/certificate.key
    cert_name: icinga-agent.localdomain
    force_newcert: false
    endpoints:
      - name: NodeName
    zones:
      - name: ZoneName
        endpoints:
          - NodeName
```
