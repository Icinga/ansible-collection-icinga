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
            apply=dict(default=False, type='bool'),
            apply_for=dict(type='str'),
            imports=dict(default=list(), type='list', elements='str'),
            display_name=dict(type='str'),
            host_name=dict(type='str'),
            groups=dict(type='list', elements='str'),
            _vars=dict(default=dict(), type='raw', aliases=['vars']),
            check_command=dict(type='str'),
            max_check_attempts=dict(type='int'),
            check_period=dict(type='str'),
            check_timeout=dict(type='str'),
            check_interval=dict(type='str'),
            retry_interval=dict(type='str'),
            enable_notification=dict(type='bool'),
            enable_active_checks=dict(type='bool'),
            enable_passive_checks=dict(type='bool'),
            enable_event_handler=dict(type='bool'),
            enable_flapping=dict(type='bool'),
            flapping_threshold_high=dict(type='float'),
            flapping_threshold_low=dict(type='float'),
            enable_perfdata=dict(type='bool'),
            event_command=dict(type='str'),
            volatile=dict(type='bool'),
            zone=dict(type='str'),
            command_endpoint=dict(type='str'),
            notes=dict(type='str'),
            notes_url=dict(type='str'),
            icon_image=dict(type='str'),
            icon_image_alt=dict(type='str'),
            assign=dict(default=list(), type='list', elements='str'),
            ignore=dict(default=list(), type='list', elements='str'),
        )
    )

    args = module.params
    name = args.pop('name')
    order = args.pop('order')
    state = args.pop('state')
    file = args.pop('file')
    template = args.pop('template')
    imports = args.pop('imports')
    apply = args.pop('apply')
    apply_for = args.pop('apply_for')
    del args['_vars']

    module.exit_json(
        changed=False,
        args=args,
        name=name,
        order=str(order),
        state=state,
        file=file,
        template=template,
        imports=imports,
        apply=apply,
        apply_for=apply_for
    )


if __name__ == '__main__':
    main()
