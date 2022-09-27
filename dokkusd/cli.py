import argparse
import os

from .deploy import Deploy


def main() -> None:
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="subparser_name")

    deploy_parser = subparsers.add_parser("deploy")

    # host
    deploy_parser.add_argument("--remotehost", help="Remote URL")
    deploy_parser.add_argument("--remoteport", help="Remote Port", default="22")
    deploy_parser.add_argument("--remoteuser", help="Remote User", default="dokku")

    # app details
    deploy_parser.add_argument("--appname", help="App name")

    args = parser.parse_args()

    if args.subparser_name == "deploy":

        deploy = Deploy(
            directory=os.getcwd(),
            remote_user=args.remoteuser,
            remote_host=args.remotehost,
            remote_port=args.remoteport,
            app_name=args.appname,
        )
        deploy.go()


if __name__ == "__main__":
    main()
