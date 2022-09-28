class ServiceConfigModel:
    def __init__(self, config, app_name):
        if isinstance(config, str):
            self.create_command = [config + ":create", app_name]
            self.link_command = [config + ":link", app_name, app_name]


class VolumeConfigModel:
    def __init__(self, config, app_name):
        if isinstance(config, str):
            self.ensure_command = ["storage:ensure-directory", app_name]
            self.mount_command = ["storage:mount", app_name, app_name + ":" + config]
