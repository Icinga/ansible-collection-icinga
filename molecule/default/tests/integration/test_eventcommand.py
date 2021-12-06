def test_icinga2_object_scheduled_downtime(host):
    i2_file = host.file("/etc/icinga2/zones.d/main/eventcommand.conf")
    print(i2_file.content_string)
    assert i2_file.is_file
    assert i2_file.contains('object EventCommand "eventcommand-test" {')
    if host.system_info.distribution == 'centos':
      assert i2_file.user == "icinga"
      assert i2_file.group == "icinga"
      assert i2_file.mode == 0o644
    if host.system_info.distribution == 'debian':
      assert i2_file.user == "nagios"
      assert i2_file.group == "nagios"
      assert i2_file.mode == 0o644
