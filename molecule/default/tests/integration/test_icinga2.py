def test_icinga2_package(host):
    icinga2_pkg = host.package("icinga2")
    assert icinga2_pkg.is_installed

def test_icinga2_dir(host):
    icinga2_dir = host.file("/etc/icinga2")
    assert icinga2_dir.is_directory

def test_icinga2_features(host):
    f_checker = host.file("/etc/icinga2/features-enabled/checker.conf")
    assert f_checker.linked_to("/etc/icinga2/features-available/checker.conf")
