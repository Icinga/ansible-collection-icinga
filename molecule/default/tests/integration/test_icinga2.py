def test_icinga2_package(host):
    icinga2_pkg = host.package("icinga2")
    assert icinga2_pkg.is_installed

def test_icinga2_configdir(host):
    icinga2_cdir = host.file("/etc/icinga2/zones.d/main")
    assert icinga2_cdir.is_directory
    if host.system_info.distribution == 'centos':
      assert icinga2_cdir.user == "icinga"
      assert icinga2_cdir.group == "icinga"
    if host.system_info.distribution == 'debian':
      assert icinga2_cdir.user == "nagios"
      assert icinga2_cdir.group == "nagios"

def test_icinga2_zones_dir(host):
    i2_zones_dir = host.file("/etc/icinga2/zones.d/main/hosts")
    if host.system_info.distribution == 'centos':
      assert i2_zones_dir.is_directory
      assert i2_zones_dir.user == "icinga"
      assert i2_zones_dir.group == "icinga"
    if host.system_info.distribution == 'debian':
      assert i2_zones_dir.is_directory
      assert i2_zones_dir.user == "nagios"
      assert i2_zones_dir.group == "nagios"

def test_icinga2_object_host(host):
    i2_file = host.file("/etc/icinga2/zones.d/main/hosts/agent.localdomain.conf")
    print(i2_file.content_string)
    assert i2_file.is_file
    assert i2_file.contains('object Zone "agent.localdomain" {')
    assert i2_file.contains('object Endpoint "agent.localdomain" {')
    assert i2_file.contains('object Host "agent.localdomain" {')
    if host.system_info.distribution == 'centos':
      assert i2_file.user == "icinga"
      assert i2_file.group == "icinga"
      assert i2_file.mode == 0o644
    if host.system_info.distribution == 'debian':
      assert i2_file.user == "nagios"
      assert i2_file.group == "nagios"
      assert i2_file.mode == 0o644

def test_icinga2_object_service(host):
    i2_file = host.file("/etc/icinga2/zones.d/main/services/services.conf")
    print(i2_file.content_string)
    assert i2_file.is_file
    assert i2_file.contains('apply Service "ping" {')
    assert i2_file.contains('template Service "generic-service" {')
    if host.system_info.distribution == 'centos':
      assert i2_file.user == "icinga"
      assert i2_file.group == "icinga"
      assert i2_file.mode == 0o644
    if host.system_info.distribution == 'debian':
      assert i2_file.user == "nagios"
      assert i2_file.group == "nagios"
      assert i2_file.mode == 0o644

def test_icinga2_certificate(host):
    i2_file = host.file("/var/lib/icinga2/certs/icinga-default.crt")
    assert i2_file.is_file
    if host.system_info.distribution == 'centos':
      assert i2_file.user == "icinga"
      assert i2_file.group == "icinga"
      assert i2_file.mode == 0o644
    if host.system_info.distribution == 'debian':
      assert i2_file.user == "nagios"
      assert i2_file.group == "nagios"
      assert i2_file.mode == 0o644

def test_icinga2_crt_key(host):
    i2_file = host.file("/var/lib/icinga2/certs/icinga-default.key")
    assert i2_file.is_file
    if host.system_info.distribution == 'centos':
      assert i2_file.user == "icinga"
      assert i2_file.group == "icinga"
      assert i2_file.mode == 0o600
    if host.system_info.distribution == 'debian':
      assert i2_file.user == "nagios"
      assert i2_file.group == "nagios"
      assert i2_file.mode == 0o600

def test_icinga2_dir(host):
    icinga2_dir = host.file("/etc/icinga2")
    assert icinga2_dir.is_directory

def test_icinga2_feature_checker(host):
    i2_file = host.file("/etc/icinga2/features-enabled/checker.conf")
    assert i2_file.exists
    assert i2_file.linked_to == "/etc/icinga2/features-available/checker.conf"
    if host.system_info.distribution == 'centos':
      assert i2_file.user == "root"
      assert i2_file.group == "root"
    if host.system_info.distribution == 'debian':
      assert i2_file.user == "root"
      assert i2_file.group == "root"

def test_icinga2_feature_mainlog(host):
    i2_file = host.file("/etc/icinga2/features-enabled/mainlog.conf")
    assert i2_file.exists
    assert i2_file.linked_to == "/etc/icinga2/features-available/mainlog.conf"
    if host.system_info.distribution == 'centos':
      assert i2_file.user == "root"
      assert i2_file.group == "root"
    if host.system_info.distribution == 'debian':
      assert i2_file.user == "root"
      assert i2_file.group == "root"

def test_icinga2_feature_api(host):
    i2_file = host.file("/etc/icinga2/features-enabled/api.conf")
    assert i2_file.exists
    assert i2_file.linked_to == "/etc/icinga2/features-available/api.conf"
    if host.system_info.distribution == 'centos':
      assert i2_file.user == "root"
      assert i2_file.group == "root"
    if host.system_info.distribution == 'debian':
      assert i2_file.user == "root"
      assert i2_file.group == "root"
