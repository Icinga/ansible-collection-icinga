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

def test_icinga2_objects(host):
    i2_oh = host.file("/etc/icinga2/zones.d/main/hosts")
    assert i2_oh.is_directory
    i2_oagent = host.file("/etc/icinga2/zones.d/main/hosts/agent.localdomain.conf")
    assert i2_oagent.is_file
    print i2_oservice.content_string
    i2_oservice = host.file("/etc/icinga2/zones.d/main/services/services.conf")
    assert i2_oservice.is_file
    print i2_oservice.content_string

def test_icinga2_dir(host):
    icinga2_dir = host.file("/etc/icinga2")
    assert icinga2_dir.is_directory

def test_icinga2_features(host):
    f_checker = host.file("/etc/icinga2/features-enabled/checker.conf")
    f_mainlog = host.file("/etc/icinga2/features-enabled/mainlog.conf")
    f_api = host.file("/etc/icinga2/features-enabled/api.conf")
    assert f_checker.exists
    assert f_checker.linked_to == "/etc/icinga2/features-available/checker.conf"
    assert f_mainlog.exists
    assert f_mainlog.linked_to == "/etc/icinga2/features-available/mainlog.conf"
    assert f_api.exists
    assert f_api.linked_to == "/etc/icinga2/features-available/api.conf"
