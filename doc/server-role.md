# Role icinga-server

The collection provides several roles to install and configure Icinga 2, the role
icinga-server will provide a ready to use role to install a main Icinga 2 server.


## Variables

To manage the Icinga 2 repos use the following variable:

```
icinga2_server_manage_repos: yes
```

For a CA Server the TicketSalt is needed, therefore mandatory.

```
icinga2_server_ticket_salt: dlsj8900dssGSQ
```

The IDO feature can be configured with these variables.

```
icinga2_server_ido_type: [ idomysql | idopgsql ]
icinga2_server_ido_host: localhost
icinga2_server_ido_port: 3306
icinga2_server_ido_user: icinga2
icinga2_server_ido_password: icinga2
icinga2_server_ido_database: icinga2
```

To configure extra features besides IDO use the following:


```
icinga2_server_features:
  - name: graphite
    host: localhost
    port: 3000

```
