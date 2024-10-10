# Available Check Commands

Here is a list of the available check commands and the packages they correspond to for Debian, RedHat and Suse based systems.

Depending on the major version some packages might not be available. For example `nagios-plugins-game` is available using Enterprise Linux **7** and **9** but not using Enterprise Linux **8**.  
A run will **not** fail because of that. Those requested checks are silently skipped.

Version specific differences in package names are also accounted for.

| Check Command Name     | Debian Package              | RedHat Package           | Suse Package                 |
| ---                    | ---                         | ---                      | ---                          |
| apt                    | monitoring-plugins-basic    | nagios-plugins-apt       | -                            |
| breeze                 | monitoring-plugins-standard | nagios-plugins-breeze    | monitoring-plugins-breeze    |
| by_ssh                 | monitoring-plugins-basic    | nagios-plugins-by_ssh    | monitoring-plugins-by_ssh    |
| clamd                  | monitoring-plugins-basic    | nagios-plugins-tcp       | nagios-plugins-tcp           |
| dhcp                   | monitoring-plugins-basic    | nagios-plugins-dhcp      | monitoring-plugins-dhcp      |
| dig                    | monitoring-plugins-standard | nagios-plugins-dig       | monitoring-plugins-dig       |
| disk                   | monitoring-plugins-basic    | nagios-plugins-disk      | monitoring-plugins-disk      |
| disk_smb               | monitoring-plugins-standard | nagios-plugins-disk_smb  | monitoring-plugins-disk_smb  |
| dns                    | monitoring-plugins-standard | nagios-plugins-dns       | monitoring-plugins-dns       |
| file_age               | monitoring-plugins-basic    | nagios-plugins-file_age  | monitoring-plugins-file_age  |
| flexlm                 | monitoring-plugins-standard | nagios-plugins-flexlm    | monitoring-plugins-flexlm    |
| fping                  | monitoring-plugins-standard | nagios-plugins-fping     | monitoring-plugins-fping     |
| fping4                 | monitoring-plugins-standard | nagios-plugins-fping     | monitoring-plugins-fping     |
| fping6                 | monitoring-plugins-standard | nagios-plugins-fping     | monitoring-plugins-fping     |
| ftp                    | monitoring-plugins-basic    | nagios-plugins-tcp       | monitoring-plugins-tcp       |
| game                   | monitoring-plugins-standard | nagios-plugins-game      | -                            |
| hostalive              | monitoring-plugins-basic    | nagios-plugins-ping      | monitoring-plugins-ping      |
| hostalive4             | monitoring-plugins-basic    | nagios-plugins-ping      | monitoring-plugins-ping      |
| hostalive6             | monitoring-plugins-basic    | nagios-plugins-ping      | monitoring-plugins-ping      |
| hpjd                   | monitoring-plugins-standard | nagios-plugins-hpjd      | monitoring-plugins-hpjd      |
| http                   | monitoring-plugins-basic    | nagios-plugins-http      | monitoring-plugins-http      |
| icmp                   | monitoring-plugins-basic    | nagios-plugins-icmp      | monitoring-plugins-icmp      |
| imap                   | monitoring-plugins-basic    | nagios-plugins-tcp       | monitoring-plugins-tcp       |
| ldap                   | monitoring-plugins-standard | nagios-plugins-ldap      | monitoring-plugins-ldap      |
| load                   | monitoring-plugins-basic    | nagios-plugins-load      | monitoring-plugins-load      |
| mailq                  | monitoring-plugins-standard | nagios-plugins-mailq     | monitoring-plugins-mailq     |
| mysql                  | monitoring-plugins-standard | nagios-plugins-mysql     | monitoring-plugins-mysql     |
| mysql_query            | monitoring-plugins-standard | nagios-plugins-mysql     | monitoring-plugins-mysql     |
| negate                 | monitoring-plugins-common   | nagios-plugins           | monitoring-plugins-common    |
| nrpe                   | nagios-nrpe-plugin          | nagios-plugins-nrpe      | monitoring-plugins-nrpe      |
| nscp                   | monitoring-plugins-basic    | nagios-plugins-nt        | monitoring-plugins-nt        |
| ntp_peer               | monitoring-plugins-basic    | nagios-plugins-ntp       | monitoring-plugins-ntp_peer  |
| ntp_time               | monitoring-plugins-basic    | nagios-plugins-ntp       | monitoring-plugins-ntp_time  |
| pgsql                  | monitoring-plugins-standard | nagios-plugins-pgsql     | monitoring-plugins-pgsql     |
| ping                   | monitoring-plugins-basic    | nagios-plugins-ping      | monitoring-plugins-ping      |
| ping4                  | monitoring-plugins-basic    | nagios-plugins-ping      | monitoring-plugins-ping      |
| ping6                  | monitoring-plugins-basic    | nagios-plugins-ping      | monitoring-plugins-ping      |
| pop                    | monitoring-plugins-basic    | nagios-plugins-tcp       | monitoring-plugins-tcp       |
| procs                  | monitoring-plugins-basic    | nagios-plugins-procs     | monitoring-plugins-procs     |
| radius                 | monitoring-plugins-standard | nagios-plugins-radius    | monitoring-plugins-radius    |
| rpc                    | monitoring-plugins-standard | nagios-plugins-rpc       | monitoring-plugins-rpc       |
| simap                  | monitoring-plugins-basic    | nagios-plugins-tcp       | monitoring-plugins-tcp       |
| smart                  | monitoring-plugins-basic    | nagios-plugins-ide_smart | monitoring-plugins-ide_smart |
| smtp                   | monitoring-plugins-basic    | nagios-plugins-smtp      | monitoring-plugins-smtp      |
| snmp                   | monitoring-plugins-standard | nagios-plugins-snmp      | monitoring-plugins-snmp      |
| snmpv3                 | monitoring-plugins-standard | nagios-plugins-snmp      | monitoring-plugins-snmp      |
| snmp-uptime            | monitoring-plugins-standard | nagios-plugins-snmp      | monitoring-plugins-snmp      |
| spop                   | monitoring-plugins-basic    | nagios-plugins-tcp       | monitoring-plugins-tcp       |
| ssh                    | monitoring-plugins-basic    | nagios-plugins-ssh       | monitoring-plugins-ssh       |
| ssl                    | monitoring-plugins-basic    | nagios-plugins-tcp       | monitoring-plugins-tcp       |
| ssmtp                  | monitoring-plugins-basic    | nagios-plugins-tcp       | monitoring-plugins-tcp       |
| swap                   | monitoring-plugins-basic    | nagios-plugins-swap      | monitoring-plugins-swap      |
| tcp                    | monitoring-plugins-basic    | nagios-plugins-tcp       | monitoring-plugins-tcp       |
| udp                    | monitoring-plugins-basic    | nagios-plugins-tcp       | monitoring-plugins-tcp       |
| ups                    | monitoring-plugins-basic    | nagios-plugins-ups       | monitoring-plugins-ups       |
| uptime                 | nagios-plugins-contrib      | nagios-plugins-uptime    | monitoring-plugins-uptime    |
| users                  | monitoring-plugins-basic    | nagios-plugins-users     | monitoring-plugins-users     |
