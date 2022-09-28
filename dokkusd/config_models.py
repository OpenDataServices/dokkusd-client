class ServiceConfigModel:
    def __init__(self, config, app_name):
        if isinstance(config, str):
            self.create_command = [config + ":create", app_name]
            self.link_command = [config + ":link", app_name, app_name]
