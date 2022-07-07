def test_icinga2_object_scheduled_downtime(host):
    i2_file = host.file("/etc/icinga2/zones.d/main/ScheduledDowntime.conf")
    print(i2_file.content_string)
    assert i2_file.is_file
    assert i2_file.contains('object ScheduledDowntime "scheduled-downtime-test" {')
    assert i2_file.contains('host_name = "agent.localdomain"')
    assert i2_file.contains('author = "icingaadmin"')
    assert i2_file.contains('comment = "Downtime"')
    assert i2_file.contains('duration = 30m')
    assert i2_file.contains('fixed = false')
    assert i2_file.contains('sunday = "02:00-03:00"')
    if host.system_info.distribution == 'centos':
      assert i2_file.user == "icinga"
      assert i2_file.group == "icinga"
      assert i2_file.mode == 0o644
    if host.system_info.distribution == 'debian':
      assert i2_file.user == "nagios"
      assert i2_file.group == "nagios"
      assert i2_file.mode == 0o644
