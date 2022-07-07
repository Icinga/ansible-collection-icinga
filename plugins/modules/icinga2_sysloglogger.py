from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(
        supports_check_mode=True,
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent']),
            name=dict(required=True),
            order=dict(default=10, type='int'),
            file=dict(default='features-available/syslog.conf', type='str'),
            severity=dict(
                default='warning',
                choices=[
                    'debug', 'notice', 'information',
                    'warning', 'critical'
                ]
            ),
            facility=dict(
                default='LOG_SYSLOG',
                choices=[
                    'LOG_AUTH', 'LOG_AUTHPRIV', 'LOG_CRON',
                    'LOG_DAEMON', 'LOG_FTP', 'LOG_KERN',
                    'LOG_LOCAL0', 'LOG_LOCAL1', 'LOG_LOCAL2',
                    'LOG_LOCAL3', 'LOG_LOCAL4', 'LOG_LOCAL5',
                    'LOG_LOCAL6', 'LOG_LOCAL7', 'LOG_LPR',
                    'LOG_MAIL', 'LOG_NEWS', 'LOG_SYSLOG',
                    'LOG_USER', 'LOG_USER'
                ]
            ),
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
