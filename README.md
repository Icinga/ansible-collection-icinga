# ansible-collection-icinga

Collection to setup and manage components of the Icinga software stack.

# Monitoring Objects Configuration

By adding the variable `icinga2_monitoring_objects` the role Icinga 2 will
generate configuration files with objects included.

The `file` key will be used to control in which zone and directory structure the object will be placed.

In addition with the `icinga2_config_location` the Files will then be created in the destination.


```
icinga2_monitoring_objects:
  - object_name: master.localdomaion
    object_type: Host
    file: master/hosts/master.localdomain.conf
    attrs:
      address: "127.0.0.1"
      check_command: hostalive
      vars:
        os: linux
  - object_name: service_ping
    object_type: Service
    file: master/hosts/master.localdomain.conf
    attrs:
      check_command: ping4
      retry_interval: 5m
  - object_name: satellite.localdomaion
    object_type: Host
    file: master/hosts/satellite.localdomain.conf
    attrs:
      address: "127.0.0.1"
      check_command: hostalive
      vars:
        os: linux

```
