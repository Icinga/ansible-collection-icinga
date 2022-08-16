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
            email=dict(type='str'),
            pager=dict(type='str'),
            _vars=dict(default=dict(), type='raw', aliases=['vars']),
            groups=dict(type='list', elements='str'),
            enable_notifications=dict(type='bool'),
            period=dict(type='str'),
            types=dict(type='list', elements='str'),
            states=dict(type='list', elements='str'),
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
