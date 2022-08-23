from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(
        supports_check_mode=True,
        argument_spec = dict(
            state                = dict(default='present', choices=['present', 'absent']),
            name                 = dict(required=True),
            order                = dict(default=10, type='int'),
            file                 = dict(default='features-available/icingadb.conf', type='str'),
            host                 = dict(type='str'),
            port                 = dict(type='int'),
            path                 = dict(type='str'),
            password             = dict(type='str'),
            enable_tls           = dict(type='bool'),
            cert_path            = dict(type='str'),
            key_path             = dict(type='str'),
            ca_path              = dict(type='str'),
            crl_path             = dict(type='str'),
            cipher_list          = dict(type='str'),
            tls_protocolmin      = dict(type='str'),
            insecure_noverify    = dict(type='bool'),
            connect_timeout      = dict(type='int'),
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
