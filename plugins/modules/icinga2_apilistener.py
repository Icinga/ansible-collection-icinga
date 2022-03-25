from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(
        supports_check_mode=True,
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent']),
            name=dict(required=True),
            order=dict(default=10, type='int'),
            file=dict(default='features-available/api.conf', type='str'),
            ticket_salt=dict(default='TicketSalt', type='str'),
            bind_host=dict(type='str'),
            bind_port=dict(type='int'),
            accept_config=dict(default=False, type='bool'),
            accept_commands=dict(default=True, type='bool'),
            max_anonymous_clients=dict(type='int'),
            cipher_list=dict(type='str'),
            tls_protocolmin=dict(type='str'),
            tls_handshake_timeout=dict(type='int'),
            access_control_allow_origin=dict(type='list', elements='str'),
            environment=dict(type='str'),
        )
    )

    args = module.params
    name = args.pop('name')
    order = args.pop('order')
    state = args.pop('state')
    file = args.pop('file')

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
