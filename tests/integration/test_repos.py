def test_repos(host, SystemInfo):
    if SystemInfo.distribution == 'debian':
      file = '/etc/apt/sources.list.d/icinga'
    if SystemInfo.distribution == 'centos':
      file = '/etc/yum.repos.d/ICINGA-release'

    repofile = host.file(file)
    assert repofile.exists
    assert repofile.is_file