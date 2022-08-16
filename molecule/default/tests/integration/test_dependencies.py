def test_icinga2_object_host(host):
    i2_file = host.file("/etc/icinga2/zones.d/main/dependencies.conf")
    print(i2_file.content_string)
    assert i2_file.is_file
    assert i2_file.contains('apply Dependency "dependency-test" to Host {')
    assert i2_file.contains('disable_checks = true')
    assert i2_file.contains('states = [ Up, ]\n')
    assert i2_file.contains('parent_host_name = "agent.localdomain"')
    assert i2_file.contains('assign where host.name == "test.localdomain"')
    if host.system_info.distribution == 'centos':
      assert i2_file.user == "icinga"
      assert i2_file.group == "icinga"
      assert i2_file.mode == 0o644
    if host.system_info.distribution == 'debian':
      assert i2_file.user == "nagios"
      assert i2_file.group == "nagios"
      assert i2_file.mode == 0o644
