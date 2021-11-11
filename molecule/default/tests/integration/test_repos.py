def test_repos(host):
    if host.system_info.distribution == 'debian':
      repofile = '/etc/apt/sources.list.d/icinga'
    if host.system_info.distribution == 'centos':
      repofile = '/etc/yum.repos.d/ICINGA-release'


    rf = host.file(repofile)
    assert rf.is_file
