## Feature API

The API Feature configures the API. The feature will manage
certificate, private key and CA certificate or will create
a certificate signing requests. It also manages the **zones.conf**.

All attributes of the object type [ApiListener](https://icinga.com/docs/icinga-2/latest/doc/09-object-types/#apilistener) can be added as keys.

All non Icinga attributes to configure the feature are explained below.

Example how to install an Agent:

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

Example how to install a master/server instance:

```
icinga2_features:
  - name: api
    force_newcert: false
    ca_host: none
    endpoints:
      - name: NodeName
    zones:
      - name: ZoneName
        endpoints:
          - NodeName
```

### Instance with Certificate Authority

To create an instance with a local CA, the API Feature parameter `ca_host` should be `none`.

```
ca_host: none
```

### Generate Certificate Signing Requests

Create Signing Request to get a certificate managed by the parameter `ca_host` and `ca_host_port`. If
set to the master/server hostname, FQDN or IP, the node setup tries to connect
via API an retrieve the trusted certificate.

> **_NOTE:_**  Ticket creation will be delegated, the host should accessible via the name or
can defined as icinga2_delegate_host to match the Ansible alias.

```
ca_host: icinga-server.localdomain
ca_host_port: 5665
```

By default the FQDN is used as certificate common name, to put a name
yourself:

```
cert_name: myown-commonname.fqdn
```

To force a new request set `force_newcert` to `true`:

```
force_newcert: true
```

### Use your own ready-made certificate

If you want to use certificates which aren't created by **Icinga 2 CA**, then use
the following variables to point the role to your own certificates.

```
ssl_ca: ca.crt
ssl_cert: certificate.crt
ssl_key: certificate.key
```

> **_NOTE:_** All three parameters have to be set otherwise a signing request is built
and `ca_host` must be defined.

The role will copy the files from your Ansible controller node to
**/var/lib/icinga2/certs** on the remote host. File names are
set to by the parameter `cert_name` (by default FQDN).

```
icinga2_features:
  - name: api
    cert_name: host.example.org
    ssl_ca: /home/ansible/certs/ca.crt
    ssl_cert: /home/ansible/certs/host.crt
    ssl_key: /home/ansible/certs/host.key
    endpoints:
      - name: NodeName
    zones:
      - name: ZoneName
        endpoints:
          - NodeName
```

### Feature variables

* `ca_host: string`
  * Use to decide where to gather the certificates. When set to **None**, Ansible will create a local Certificate Authority on the Host. Use **hostname** or **ipaddress** as value.

* `force_newcert: boolean`
  * Force new certificates on the destination hosts.

* `cert_name: string`
  * Common name of Icinga client/server instance. Default is **ansible_fqdn**.

* `ssl_ca: string`
  * Path to the ca file when using manual certificates

* `ssl_cert: string`
  * Path to the certificate file when using manual certificates.

* `ssl_key: string`
  * Path to the certificate key file when using manual certificates.

* `endpoints: list of dicts`
  * Defines endpoints in **zones.conf**, each endpoint is required to have a name and optional a host or port.  
    * `name: string`
    * `host: string`
    * `port: number`

* `zones: list of dicts`
  * Defines zones in **zones.conf**, each zones is required to have a name and endpoints. The parameter global is optional.
    * `name: string`
    * `endpoints: list`
    * `global: boolean`
