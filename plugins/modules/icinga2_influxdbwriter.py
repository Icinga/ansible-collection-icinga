from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(
        supports_check_mode=True,
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent']),
            name=dict(required=True),
            order=dict(default=10, type='int'),
            file=dict(default='features-available/influxdb.conf', type='str'),
            host=dict(type='str'),
            port=dict(type='int'),
            database=dict(type='str'),
            username=dict(type='str'),
            password=dict(type='str'),
            ssl_enable=dict(type='bool'),
            ssl_ca_cert=dict(type='str'),
            ssl_cert=dict(type='str'),
            ssl_key=dict(type='str'),
            ssl_insecure_noverify=dict(type='bool'),
            basic_auth=dict(type='dict'),
            host_template=dict(type='dict'),
            service_template=dict(type='dict'),
            enable_send_thresholds=dict(type='bool'),
            enable_send_metadata=dict(type='bool'),
            flush_interval=dict(type='str'),
            flush_threshold=dict(type='int'),
            enable_ha=dict(type='bool'),
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
