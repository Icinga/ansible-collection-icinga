from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(
        supports_check_mode=True,
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent']),
            name=dict(required=True),
            order=dict(default=10, type='int'),
            file=dict(default='zones.conf', type='str'),
            enable_notifications=dict(type='bool'),
            enable_event_handlers=dict(type='bool'),
            enable_flapping=dict(type='bool'),
            enable_host_checks=dict(type='bool'),
            enable_service_checks=dict(type='bool'),
            enable_perfdata=dict(type='bool'),
            environment=dict(type='str'),
            _vars=dict(default=dict(), type='raw', aliases=['vars']),
        )
    )

    args = module.params
    name = args.pop('name')
    order = args.pop('order')
    state = args.pop('state')
    file = args.pop('file')
    del args['_vars']

    module.exit_json(
        changed=False,
        args=args,
        name=name,
        order=str(order),
        state=state,
        file=file
    )


if __name__ == '__main__':
    main()
