from shlex import quote


class ServiceConfigModel:
    def __init__(self, config, app_name):
        if isinstance(config, str):
            self.create_command = [config + ":create", app_name]
            self.link_command = [config + ":link", app_name, app_name]


class VolumeConfigModel:
    def __init__(self, config, app_name):
        if isinstance(config, str):
            self.ensure_command = ["storage:ensure-directory", app_name]
            self.mount_command = [
                "storage:mount",
                app_name,
                "/var/lib/dokku/data/storage/" + app_name + ":" + config,
            ]
        elif isinstance(config, dict):
            storage_sub_dir_name = app_name + "_" + config.get("host_subdir")
            container_path = config.get("container_path")
            self.ensure_command = ["storage:ensure-directory", storage_sub_dir_name]
            self.mount_command = [
                "storage:mount",
                app_name,
                "/var/lib/dokku/data/storage/"
                + storage_sub_dir_name
                + ":"
                + container_path,
            ]


class EnvironmentVariableConfigModel:
    def __init__(self, key, value, app_name):
        self.set_command = [
            "config:set",
            "--no-restart",
            app_name,
            key + "=" + quote(value),
        ]
