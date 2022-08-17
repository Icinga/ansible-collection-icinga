def test_repos(host):
    if host.system_info.distribution == 'debian':
      repofile = host.file("/etc/apt/sources.list.d/icinga.list")
      assert repofile.is_file
      assert repofile.user == "root"
    if host.system_info.distribution == 'centos':
      repofile = host.file("/etc/yum.repos.d/ICINGA-release.repo")
      assert repofile.is_file
      assert repofile.user == "root"
