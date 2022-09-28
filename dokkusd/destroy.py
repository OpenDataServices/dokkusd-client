from .util import Task


class Destroy(Task):
    def go(self) -> None:

        # --------------------- Destroy app
        print("Destroy app ...")
        stdout, stderr = self._dokku_command(["dokkusd:destroy-cascade", self.app_name])
        print(stdout)
        print(stderr)
