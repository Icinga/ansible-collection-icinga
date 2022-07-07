#!/usr/bin/python


from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(
        supports_check_mode=True,
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent']),
            name=dict(required=True),
            order=dict(default=10, type='int'),
            file=dict(required=True, type='str'),
            template=dict(default=False, type='bool'),
            imports=dict(default=list(), type='list', elements='str'),
            display_name=dict(type='str'),
            address=dict(type='str'),
            address6=dict(type='str'),
            groups=dict(type='list', elements='str'),
            _vars=dict(default=dict(), type='raw', aliases=['vars']),
            check_command=dict(type='str'),
            max_check_attempts=dict(type='int'),
            check_period=dict(type='str'),
            check_timeout=dict(type='str'),
            check_interval=dict(type='str'),
            retry_interval=dict(type='str'),
            enable_notifications=dict(type='bool'),
            enable_active_checks=dict(type='bool'),
            enable_passive_checks=dict(type='bool'),
            enable_event_handler=dict(type='bool'),
            enable_flapping=dict(type='bool'),
            enable_perfdata=dict(type='bool'),
            event_command=dict(type='str'),
            flapping_threshold_high=dict(type='float'),
            flapping_threshold_low=dict(type='float'),
            volatile=dict(type='bool'),
            zone=dict(type='str'),
            command_endpoint=dict(type='str'),
            notes=dict(type='str'),
            notes_url=dict(type='str'),
            action_url=dict(type='str'),
            icon_image=dict(type='str'),
            icon_image_alt=dict(type='str'),
        )
    )

    args = module.params
    name = args.pop('name')
    order = args.pop('order')
    state = args.pop('state')
    file = args.pop('file')
    template = args.pop('template')
    imports = args.pop('imports')
    del args['_vars']

    module.exit_json(
        changed=False,
        args=args,
        name=name,
        order=str(order),
        state=state,
        file=file,
        template=template,
        imports=imports
    )


if __name__ == '__main__':
    main()
