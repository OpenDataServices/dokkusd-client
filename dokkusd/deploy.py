import json
import os
import subprocess

from .config_models import ServiceConfigModel, VolumeConfigModel
from .util import Task


class Deploy(Task):
    def go(self) -> None:

        # --------------------- app.json
        app_json_name = os.path.join(self.directory, "app.json")
        app_json = {}
        if os.path.exists(app_json_name):
            with open(app_json_name) as fp:
                app_json = json.load(fp)

        # --------------------- git remote
        print("Configure git remote ...")
        git_remote_name = self._get_git_remote_name()

        # --------------------- Create app
        print("Create app ...")
        stdout, stderr = self._dokku_command(["apps:create", self.app_name])
        print(stdout)
        print(stderr)

        # --------------------- Services
        print("Configure services ...")
        services = app_json.get("dokkusd", {}).get("services", [])
        for service in services:
            service_model = ServiceConfigModel(service, self.app_name)
            stdout, stderr = self._dokku_command(service_model.create_command)
            print(stdout)
            print(stderr)
            stdout, stderr = self._dokku_command(service_model.link_command)
            print(stdout)
            print(stderr)

        # --------------------- Volumes
        print("Configure volumes ...")
        volumes = app_json.get("dokkusd", {}).get("volumes", [])
        for volume in volumes:
            volume_model = VolumeConfigModel(volume, self.app_name)
            stdout, stderr = self._dokku_command(volume_model.ensure_command)
            print(stdout)
            print(stderr)
            stdout, stderr = self._dokku_command(volume_model.mount_command)
            print(stdout)
            print(stderr)

        # --------------------- Deploy
        print("Deploy ...")
        process = subprocess.Popen(
            ["git", "push", git_remote_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=self.directory,
        )
        stdout, stderr = process.communicate()
        print(stdout.decode("utf-8"))
        print(stderr.decode("utf-8"))
