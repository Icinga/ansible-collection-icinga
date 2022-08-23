from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(
        supports_check_mode=True,
        argument_spec = dict(
            state                = dict(default='present', choices=['present', 'absent']),
            name                 = dict(required=True),
            order                = dict(default=10, type='int'),
            file                 = dict(default='features-available/livestatus.conf', type='str'),
            socket_type          = dict(type='str', choices=['tcp', 'unix']),
            bind_host            = dict(type='str'),
            bind_port            = dict(type='int'),
            socket_path          = dict(type='str'),
            compat_log_path      = dict(type='str'),
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
