def test_icingadb_config(host):
    i2_file = host.file("/etc/icingadb/config.yml")
    assert i2_file.is_file
    assert i2_file.contains('  history-days: 10')
    assert i2_file.contains('  sla-days: 11')
    assert i2_file.contains('    acknowledgement: 20')
    assert i2_file.contains('    comment: 30')
    assert i2_file.contains('    state: 60')
    assert i2_file.contains('    downtime: 10')
    assert i2_file.contains('    notification: 4')
    assert i2_file.contains('    flapping: 2')
