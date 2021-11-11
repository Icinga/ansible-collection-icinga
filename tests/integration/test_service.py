def test_icinga2_service(host):
    service = host.service("icinga2")
    assert service.is_running
    assert service.is_enabled
