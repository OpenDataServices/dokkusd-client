from dokkusd.config_models import VolumeConfigModel


def test_string_1():
    c = VolumeConfigModel(config="/storage", app_name="app_name")
    assert c.ensure_command == ["storage:ensure-directory", "app_name"]
    assert c.mount_command == [
        "storage:mount",
        "app_name",
        "/var/lib/dokku/data/storage/app_name:/storage",
    ]


def test_dict_1():
    c = VolumeConfigModel(
        config={"host_subdir": "database", "container_path": "/database"},
        app_name="app_name",
    )
    assert c.ensure_command == ["storage:ensure-directory", "app_name_database"]
    assert c.mount_command == [
        "storage:mount",
        "app_name",
        "/var/lib/dokku/data/storage/app_name_database:/database",
    ]
