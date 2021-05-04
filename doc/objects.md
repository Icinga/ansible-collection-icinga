# Monitoring Objects Configuration

## Objects

By adding the variable `icinga2_objects` the role Icinga 2 will
generate configuration files with objects included.

This variable consists of Icinga 2 object attributes and attributes refering to the file created in the processs.

The second level of the dictionary tells on which host the configuration is created. All objects in the example below, will be created on the given host.: `host.example.org`.

The `file` key will be used to control in which directory structure the object will be placed.
In addition the `order` key will decide the order of the objects which are part of the file.
The default for `order` is set to 10, so everything below that number will be in front of the file, all objects with the order above 10 will be placed later in the file.

The `type` will be the original Icinga 2 object types, a list of all can be found in the documentation. [Icinga 2 Monitoring Objects](https://icinga.com/docs/icinga-2/latest/doc/09-object-types/#monitoring-objects)



```
icinga2_objects:
  host.example.org:
    - name: "{{ ansible_fqdn }}"
      type: Endpoint
      file: "{{ 'conf.d/' + ansible_hostname + '.conf' }}"
      order: 20
    - name: "{{ ansible_fqdn }}"
      type: Zone
      file: "{{ 'conf.d/' + ansible_hostname + '.conf' }}"
      order: 20
      endpoints:
        - "{{ ansible_fqdn }}"
      parent: main
```
## Managing Config directories

To create or prepare the directories for the monitoring configuration use the variable `icinga2_config_directories`.
Those directories are only managed when they are part of `zones.d`, `conf.d` or the variable `icinga2_confd`.

```
icinga2_config_directories:
  - zones.d/main/hosts/
  - zones.d/main/services/
  - conf.d/commands/
```
