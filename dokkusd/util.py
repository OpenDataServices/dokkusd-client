import subprocess


def get_remote_name_of_url(git_remote_verbose_output, url_wanted):
    for line in git_remote_verbose_output.split("\n"):
        line_bits = [i.strip() for i in line.split() if i.strip()]
        if line_bits and line_bits[1] == url_wanted:
            return line_bits[0]


class Task:
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

    def _get_git_remote_name(self):
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
        return git_remote_name
