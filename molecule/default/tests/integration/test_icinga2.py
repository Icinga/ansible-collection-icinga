def test_icinga2_package(host):
    icinga2_pkg = host.package("icinga2")
    assert icinga2_pkg.is_installed

def test_icinga2_dir(host):
    icinga2_dir = host.file("/etc/icinga2")
    assert icinga2_dir.is_directory
