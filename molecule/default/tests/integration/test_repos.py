def test_repos(host):
    if host.system_info.distribution == 'debian':
      file = '/etc/icinga2/icinga2.conf'
    if host.system_info.distribution == 'centos':
      file = '/etc/icinga2/icinga2.conf'


    repofile = host.file(file)
    assert repofile.exists
