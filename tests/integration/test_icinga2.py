def test_icinga2_package(host, system_info):
    icinga2_pkg = host.package("icinga2")
    assert icinga2_pkg.is_installed
