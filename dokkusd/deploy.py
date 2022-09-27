import json
import os
import subprocess

from .util import get_remote_name_of_url


class Deploy:
    def __init__(
        self,
        directory: str,
        remote_user: str,
        remote_host: str,
        remote_port: str,
        app_name: str,
    ):
        self.directory = directory
        self.remote_user = remote_user
        self.remote_host = remote_host
        self.remote_port = remote_port
        self.app_name = app_name

    def _dokku_command(self, command):
        full_command = [
            "ssh",
            "-p" + self.remote_port,
            self.remote_user + "@" + self.remote_host,
        ]
        full_command.extend(command)
        process = subprocess.Popen(
            full_command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=self.directory,
        )
        stdout, stderr = process.communicate()
        return stdout.decode("utf-8"), stderr.decode("utf-8")

    def go(self) -> None:

        # --------------------- app.json
        app_json_name = os.path.join(self.directory, "app.json")
        app_json = {}
        if os.path.exists(app_json_name):
            with open(app_json_name) as fp:
                app_json = json.load(fp)

        # --------------------- git remote
        print("Configure git remote ...")
        git_remote_url: str = (
            "ssh://"
            + self.remote_user
            + "@"
            + self.remote_host
            + ":"
            + self.remote_port
            + "/"
            + self.app_name
        )

        process = subprocess.Popen(
            ["git", "remote", "-v"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=self.directory,
        )
        stdout, stderr = process.communicate()

        # TODO check stderr

        git_remote_name = get_remote_name_of_url(stdout.decode("utf-8"), git_remote_url)
        if not git_remote_name:
            # TODO find unique git remote name
            git_remote_name = "dokku"
            process = subprocess.Popen(
                ["git", "remote", "add", git_remote_name, git_remote_url],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=self.directory,
            )
            stdout, stderr = process.communicate()

        # --------------------- Create app
        print("Create app ...")
        stdout, stderr = self._dokku_command(["apps:create", self.app_name])
        print(stdout)
        print(stderr)

        # --------------------- Create app
        print("Configure services ...")
        services = app_json.get("dokkusd", {}).get("services", [])
        for service in services:
            stdout, stderr = self._dokku_command([service + ":create", self.app_name])
            print(stdout)
            print(stderr)
            stdout, stderr = self._dokku_command(
                [service + ":link", self.app_name, self.app_name]
            )
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
