from dokkusd.config_models import CommandConfigModel


def test_valid_1():
    c = CommandConfigModel(
        config=["nginx:set", "$APP_NAME", "client-max-body-size", "50m"],
        app_name="app_name",
    )
    assert c.valid
    assert c.command == [
        "nginx:set",
        "app_name",
        "client-max-body-size",
        "50m",
    ]


def test_not_valid_1():
    c = CommandConfigModel(config=["apps:list"], app_name="app_name")
    assert not c.valid
