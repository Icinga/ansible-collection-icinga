# Ansible Role icinga.icinga.repos

This role configures Icinga 2 related repositories to provide all necessary packages.


## Variables

To enable the EPEL repository.

```
icinga_repo_epel: true
icinga_repo_scl: true
```

To manage which Icinga Repos to use the following variables: 

```
icinga_repo_stable: true
icinga_repo_testing: false
icinga_repo_snapshot: false
```
