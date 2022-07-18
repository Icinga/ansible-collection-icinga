from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(
        supports_check_mode=True,
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent']),
            name=dict(required=True),
            order=dict(default=10, type='int'),
            file=dict(default='features-available/ido-mysql.conf', type='str'),
            host=dict(default='localhost', type='str'),
            port=dict(default='5432', type='int'),
            user=dict(default='icinga2', type='str'),
            password=dict(required=True, type='str'),
            database=dict(default='icinga2', type='str'),
            ssl_mode=dict(choices=['prefer', 'require', 'verify-ca', 'verify-full', 'allow', 'disable']),
            ssl_key=dict(type='str'),
            ssl_cert=dict(type='str'),
            ssl_ca=dict(type='str'),
            table_prefix=dict(type='str'),
            instance_name=dict(type='str'),
            instance_description=dict(type='str'),
            enable_ha=dict(type='bool'),
            failover_timeout=dict(type='str'),
            cleanup=dict(type='dict'),
            categories=dict(type='list', elements='str'),
            import_schema=dict(type='bool'),
        )
    )

    args = module.params
    name = args.pop('name')
    order = args.pop('order')
    state = args.pop('state')
    file = args.pop('file')
    if 'import_schema' in args:
        args.pop('import_schema')

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
