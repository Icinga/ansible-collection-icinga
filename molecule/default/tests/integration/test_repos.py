def test_repos(host):
    if host.system_info.distribution == 'debian':
      repofile = host.file("etc/apt/sources.list.d/icinga")
    if host.system_info.distribution == 'centos':
      repofile = host.file("/etc/yum.repos.d/ICINGA-release")

    assert repofile.is_file
