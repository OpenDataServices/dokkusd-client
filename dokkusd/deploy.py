import json
import os
import subprocess

from .config_models import (
    EnvironmentVariableConfigModel,
    ServiceConfigModel,
    VolumeConfigModel,
)
from .util import Task


class Deploy(Task):
    def __init__(
        self,
        directory: str,
        remote_user: str,
        remote_host: str,
        remote_port: str,
        app_name: str,
        http_auth_user: str = None,
        http_auth_password: str = None,
        environment_variables_json_string: str = None,
        environment_variables: dict = {},
    ):
        super().__init__(
            directory=directory,
            remote_user=remote_user,
            remote_host=remote_host,
            remote_port=remote_port,
            app_name=app_name,
        )
        self.http_auth_user = http_auth_user
        self.http_auth_password = http_auth_password
        self._environment_variables: dict = environment_variables
        self.environment_variables_json_string = environment_variables_json_string

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

        # --------------------- Env Vars
        print("Configure Environment Variables ...")
        envvars = app_json.get("dokkusd", {}).get("environment_variables", {})
        envvars.update(self._environment_variables)
        if self.environment_variables_json_string:
            environment_variables_dict = json.loads(
                self.environment_variables_json_string
            )
            envvars.update(environment_variables_dict)
        for key, value in envvars.items():
            environment_variable = EnvironmentVariableConfigModel(
                key, value, self.app_name
            )
            stdout, stderr = self._dokku_command(environment_variable.set_command)
            print(stdout)
            print(stderr)

        # --------------------- HTTP Auth
        if self.http_auth_user and self.http_auth_password:
            print("HTTP Auth ...")
            stdout, stderr = self._dokku_command(
                [
                    "http-auth:enable",
                    self.app_name,
                    self.http_auth_user,
                    self.http_auth_password,
                ]
            )
            print(stdout)
            print(stderr)

        # --------------------- Keep Git Dir
        if "keep_git_dir" in app_json.get("dokkusd", {}):
            print("Keep Git Dir ...")
            stdout, stderr = self._dokku_command(
                [
                    "git:set",
                    self.app_name,
                    "keep-git-dir",
                    "true" if app_json["dokkusd"]["keep_git_dir"] else "false",
                ]
            )
            print(stdout)
            print(stderr)

        # --------------------- Nginx
        if "nginx" in app_json.get("dokkusd", {}):
            nginx = app_json.get("dokkusd", {}).get("nginx")
            if isinstance(nginx, dict):
                if "client_max_body_size" in nginx:
                    print("Nginx: client-max-body-size ...")
                    stdout, stderr = self._dokku_command(
                        [
                            "nginx:set",
                            self.app_name,
                            "client-max-body-size",
                            str(nginx.get("client_max_body_size")),
                        ]
                    )
                    print(stdout)
                    print(stderr)

        # --------------------- Deploy
        print("Deploy ...")
        process = subprocess.Popen(
            ["git", "push", "-f", git_remote_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=self.directory,
        )
        stdout, stderr = process.communicate()
        print(stdout.decode("utf-8"))
        print(stderr.decode("utf-8"))
