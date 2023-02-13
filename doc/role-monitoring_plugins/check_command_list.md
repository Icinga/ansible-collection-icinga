# Available Check Commands

Here is a list of the available check commands and the packages they correspond to for Debian and RedHat based systems.  

Depending on the major version some packages might not be available. For example `nagios-plugins-game` is available using Enterprise Linux **7** and **9** but not using Enterprise Linux **8**.  
A run will **not** fail because of that. Those requested checks are silently skipped.  

Version specific differences in package names are also accounted for.  

| Check Command Name     | Debian Package              | RedHat Package           |
| ---                    | ---                         | ---                      |
| apt                    | monitoring-plugins-basic    | nagios-plugins-apt       |
| breeze                 | monitoring-plugins-standard | nagios-plugins-breeze    |
| by_ssh                 | monitoring-plugins-basic    | nagios-plugins-by_ssh    |
| clamd                  | monitoring-plugins-basic    | nagios-plugins-tcp       |
| dhcp                   | monitoring-plugins-basic    | nagios-plugins-dhcp      |
| dig                    | monitoring-plugins-standard | nagios-plugins-dig       |
| disk                   | monitoring-plugins-basic    | nagios-plugins-disk      |
| disk_smb               | monitoring-plugins-standard | nagios-plugins-disk_smb  |
| dns                    | monitoring-plugins-standard | nagios-plugins-dns       |
| file_age               | monitoring-plugins-basic    | nagios-plugins-file_age  |
| flexlm                 | monitoring-plugins-standard | nagios-plugins-flexlm    |
| fping                  | monitoring-plugins-standard | nagios-plugins-fping     |
| fping4                 | monitoring-plugins-standard | nagios-plugins-fping     |
| fping6                 | monitoring-plugins-standard | nagios-plugins-fping     |
| ftp                    | monitoring-plugins-basic    | nagios-plugins-tcp       |
| game                   | monitoring-plugins-standard | nagios-plugins-game      |
| hostalive              | monitoring-plugins-basic    | nagios-plugins-ping      |
| hostalive4             | monitoring-plugins-basic    | nagios-plugins-ping      |
| hostalive6             | monitoring-plugins-basic    | nagios-plugins-ping      |
| hpjd                   | monitoring-plugins-standard | nagios-plugins-hpjd      |
| http                   | monitoring-plugins-basic    | nagios-plugins-http      |
| icmp                   | monitoring-plugins-basic    | nagios-plugins-icmp      |
| imap                   | monitoring-plugins-basic    | nagios-plugins-tcp       |
| ldap                   | monitoring-plugins-standard | nagios-plugins-ldap      |
| load                   | monitoring-plugins-basic    | nagios-plugins-load      |
| mailq                  | monitoring-plugins-standard | nagios-plugins-mailq     |
| mysql                  | monitoring-plugins-standard | nagios-plugins-mysql     |
| mysql_query            | monitoring-plugins-standard | nagios-plugins-mysql     |
| negate                 | monitoring-plugins-common   | nagios-plugins           |
| nrpe                   | nagios-nrpe-plugin          | nagios-plugins-nrpe      |
| nscp                   | monitoring-plugins-basic    | nagios-plugins-nt        |
| ntp_peer               | monitoring-plugins-basic    | nagios-plugins-ntp       |
| ntp_time               | monitoring-plugins-basic    | nagios-plugins-ntp       |
| pgsql                  | monitoring-plugins-standard | nagios-plugins-pgsql     |
| ping                   | monitoring-plugins-basic    | nagios-plugins-ping      |
| ping4                  | monitoring-plugins-basic    | nagios-plugins-ping      |
| ping6                  | monitoring-plugins-basic    | nagios-plugins-ping      |
| pop                    | monitoring-plugins-basic    | nagios-plugins-tcp       |
| procs                  | monitoring-plugins-basic    | nagios-plugins-procs     |
| radius                 | monitoring-plugins-standard | nagios-plugins-radius    |
| rpc                    | monitoring-plugins-standard | nagios-plugins-rpc       |
| simap                  | monitoring-plugins-basic    | nagios-plugins-tcp       |
| smart                  | monitoring-plugins-basic    | nagios-plugins-ide_smart |
| smtp                   | monitoring-plugins-basic    | nagios-plugins-smtp      |
| snmp                   | monitoring-plugins-standard | nagios-plugins-snmp      |
| snmpv3                 | monitoring-plugins-standard | nagios-plugins-snmp      |
| snmp-uptime            | monitoring-plugins-standard | nagios-plugins-snmp      |
| spop                   | monitoring-plugins-basic    | nagios-plugins-tcp       |
| ssh                    | monitoring-plugins-basic    | nagios-plugins-ssh       |
| ssl                    | monitoring-plugins-basic    | nagios-plugins-tcp       |
| ssmtp                  | monitoring-plugins-basic    | nagios-plugins-tcp       |
| swap                   | monitoring-plugins-basic    | nagios-plugins-swap      |
| tcp                    | monitoring-plugins-basic    | nagios-plugins-tcp       |
| udp                    | monitoring-plugins-basic    | nagios-plugins-tcp       |
| ups                    | monitoring-plugins-basic    | nagios-plugins-ups       |
| uptime                 | nagios-plugins-contrib      | nagios-plugins-uptime    |
| users                  | monitoring-plugins-basic    | nagios-plugins-users     |
