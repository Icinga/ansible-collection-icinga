# Ansible Role icinga.icinga.repos

This role configures Icinga 2 related repositories to provide all necessary packages.


## Variables

To enable the EPEL repository.

```
repos_icinga_epel: true
repos_icinga_scl: true
```

To manage which Icinga Repos to use the following variables: 

```
repos_icinga_stable: true
repos_icinga_testing: false
repos_icinga_snapshot: false
```

To use the Icinga Repository Subscription:

```
repos_icinga_subscription_username: "Your username"
repos_icinga_subscription_password: "Your password"
```
