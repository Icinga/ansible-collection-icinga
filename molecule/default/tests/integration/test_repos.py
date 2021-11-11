def test_repos(host):
    if host.system_info.distribution == 'debian':
      file = '/etc/apt/sources.list.d/icinga'
    if host.system_info.distribution == 'centos':
      file = '/etc/yum.repos.d/ICINGA-release'
    

    repofile = host.file(file)
    assert repofile.exists
    assert repofile.is_file
