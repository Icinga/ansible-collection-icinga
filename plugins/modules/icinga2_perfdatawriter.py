from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = '''
    name: icinga2_perfdatawriter
'''

def main():
    module = AnsibleModule(
        supports_check_mode=True,
        argument_spec = dict(
            state                   = dict(default='present', choices=['present', 'absent']),
            name                    = dict(required=True),
            order                   = dict(default=10, type='int'),
            file                    = dict(default='features-available/perfdata.conf', type='str'),
            host_perfdata_path      = dict(type='str'),
            service_perfdata_path   = dict(type='str'),
            host_temp_path          = dict(type='str'),
            service_temp_path       = dict(type='str'),
            host_format_template    = dict(type='str'),
            service_format_template = dict(type='str'),
            rotation_interval       = dict(type='str'),
            enable_ha               = dict(type='bool'),
        )
    )

    args = module.params
    name = args.pop('name')
    order = args.pop('order')
    state = args.pop('state')
    file = args.pop('file')

    module.exit_json(changed=False, args=args, name=name, order=str(order), state=state, file=file)

if __name__ == '__main__':
    main()
