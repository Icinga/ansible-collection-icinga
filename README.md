# ansible-collection-icinga

Collection to setup and manage components of the Icinga software stack.

# Monitoring Objects Configuration

By adding the variable `icinga2_objects` the role Icinga 2 will
generate configuration files with objects included.

The second level ot the dictionary tells on which host the configuration is to be made. Both objects below goes to host `host.example.org`.

The `file` key will be used to control in which directory structure the object will be placed.

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
