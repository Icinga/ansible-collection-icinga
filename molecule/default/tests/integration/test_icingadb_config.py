def test_icinga2_feature_icingadb(host):
    i2_file = host.file("/etc/icinga2/features-available/icingadb.conf")
    i2_link = host.file("/etc/icinga2/features-enabled/icingadb.conf")
    assert i2_file.exists
    assert i2_link.linked_to == "/etc/icinga2/features-available/icingadb.conf"
    assert i2_file.contains('object IcingaDB "icingadb" {')
    if host.system_info.distribution == 'centos':
      assert i2_file.user == "icinga"
      assert i2_file.group == "icinga"
    if host.system_info.distribution == 'debian':
      assert i2_file.user == "nagios"
      assert i2_file.group == "nagios"
