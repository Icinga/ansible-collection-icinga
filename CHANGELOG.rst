===========================
Icinga.Icinga Release Notes
===========================

.. contents:: Topics


v0.3.2
======

Release Summary
---------------

This is a bugfix release, bringing two QOL features and a fix for the installation process of some of the roles which broke with v0.3.1.

Minor Changes
-------------

- Added possibility to delegate ticket creation to satellites
- Adjusted the installation of the director module when using the source installation.

Bugfixes
--------

- Role repos: Fix bug in variable search - thanks to @gianmarco-mameli #224

v0.3.1
======

Major Changes
-------------

- Added Installation of Business Process Modeling Module

Minor Changes
-------------

- Adds password capabilities to icingadb-redis configuration (#202)
- support Raspbian armhf repos (#203)

Bugfixes
--------

- Fix incorrect behaviour within `monitoring_plugins` that lead to a cycle of installation and removal of the same packages within one play
- Fix incorrect templating when passing integers in some parts of the Icinga Web 2 configuration.
- Fix to use correct URL for Debian Ubuntu (#195)
- Fixed typo in api.yml file (exits to exists)
- Role Icingaweb2: Adjust preferences setting to store preferences in database

v0.3.0
======

Major Changes
-------------

- Add Installation on Suse Systems
- Add TLS support to import schema for mysql and psql features
- Add a role for the installation and configuration of icingadb.
- Add a role for the installation and configuration of icingadb_redis.
- Add a role for the installation and configuration of icingaweb2.
- Add a role for the installation of the monitoring plugins as listed in the Icinga Template Library
- Add the ability to use the Icinga Repository Subscription on RedHat based distributions
- Manage Module Icinga Director
- Manage Module IcingaDB

Minor Changes
-------------

- Role Repos: Change manual epel handling to package #151
- The icinga2 role wrongly include parent vars file instead of its own #148

Bugfixes
--------

- Changed parameter enable_notification to enable_notifications
- Fix variable usage in icingaweb2_modules dict thx @Alpha041087
- Fixed usage of pgsql commands and imports thx @Alpha041087
- Prevent empty config directories to always be recreated
- Use lookup plugin to load icinga2_objects to support existing variables

v0.2.1
======

Release Summary
---------------

This is a bugfix release

Bugfixes
--------

- Fix bug in default filter for icinga2_ca_host
- Fix non-idenpotence during feature disabling

v0.2.0
======

Release Summary
---------------

This is the second major release

Major Changes
-------------

- Add custom config files
- Add icinga2_config_host var
- Add management of CA Host port
- Add object and feature Influxdb2Writer
- Add object and feature LiveStatusListener
- Add object and feature for ElasticsearchWriter
- Add object and feature for GelfWriter
- Add object and feature for IcingaDB
- Add object and feature for OpenTsdbWriter
- Add object and feature for PerfdataWriter
- Add support for Fedora
- Add support for icinga2_objects var outside of hostvars
- Add validation of CA fingerprint during certificate requests

Minor Changes
-------------

- Add CONTRIBUTING.md
- Add bullseye to supported OS and fix license in role metadata
- Add pylint to CI Workflows
- Added documentation for custom config
- Rework documentation structure
- Update documentation

Bugfixes
--------

- Fix Date type error
- Fix empty custom config
- Use correct version number into examples

v0.1.0
======

Release Summary
---------------

This is the initial release
