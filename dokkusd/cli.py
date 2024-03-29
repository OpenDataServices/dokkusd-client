import argparse
import os
import sys

from .deploy import Deploy
from .destroy import Destroy


def main() -> None:
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="subparser_name")

    ### Deploy
    deploy_parser = subparsers.add_parser("deploy")

    # host
    deploy_parser.add_argument(
        "--remotehost", help="Remote URL", default=os.getenv("DOKKUSD_REMOTE_HOST")
    )
    deploy_parser.add_argument(
        "--remoteport",
        help="Remote Port",
        default=os.getenv("DOKKUSD_REMOTE_PORT") or "22",
    )
    deploy_parser.add_argument(
        "--remoteuser",
        help="Remote User",
        default=os.getenv("DOKKUSD_REMOTE_USER") or "dokku",
    )

    # app details
    deploy_parser.add_argument(
        "--appname", help="App name", default=os.getenv("DOKKUSD_APP_NAME")
    )
    deploy_parser.add_argument(
        "--httpauthuser",
        help="HTTP Auth User",
        default=os.getenv("DOKKUSD_HTTP_AUTH_USER"),
    )
    deploy_parser.add_argument(
        "--httpauthpassword",
        help="HTTP Auth Password",
        default=os.getenv("DOKKUSD_HTTP_AUTH_PASSWORD"),
    )
    deploy_parser.add_argument(
        "--environmentvariablesjson",
        help="Environment Variables in JSON dictionary",
        default=os.getenv("DOKKUSD_ENVIRONMENT_VARIABLES_JSON"),
    )
    deploy_parser.add_argument(
        "--environmentvariablesprefixedby",
        help="Any Environmental variables prefixed with this will be given to the Dokku app.",
    )
    deploy_parser.add_argument(
        "--nginxclientmaxbodysize",
        help="Sets a value for Nginx Client Max Body Size. Include units eg 50m",
        default=os.getenv("DOKKUSD_NGINX_CLIENT_MAX_BODY_SIZE"),
    )

    deploy_parser.add_argument(
        "--nginxproxyreadtimeout",
        help="Sets a value for Nginx Proxy Read Timeout. Include units eg 120s",
        default=os.getenv("DOKKUSD_NGINX_PROXY_READ_TIMEOUT"),
    )
    deploy_parser.add_argument(
        "--psscale",
        help="Sets values for scale command. eg web=1 worker=2",
        default=os.getenv("DOKKUSD_PS_SCALE"),
    )
    deploy_parser.add_argument(
        "--letsencryptemail",
        help="Set email address for Lets Encrypt. If present, Lets Encrypt will be enabled.",
        default=os.getenv("DOKKUSD_LETSENCRYPT_EMAIL"),
    )

    ### Destroy
    destroy_parser = subparsers.add_parser("destroy")
    # host
    destroy_parser.add_argument(
        "--remotehost", help="Remote URL", default=os.getenv("DOKKUSD_REMOTE_HOST")
    )
    destroy_parser.add_argument(
        "--remoteport",
        help="Remote Port",
        default=os.getenv("DOKKUSD_REMOTE_PORT") or "22",
    )
    destroy_parser.add_argument(
        "--remoteuser",
        help="Remote User",
        default=os.getenv("DOKKUSD_REMOTE_USER") or "dokku",
    )

    # app details
    destroy_parser.add_argument(
        "--appname", help="App name", default=os.getenv("DOKKUSD_APP_NAME")
    )

    ### Go
    args = parser.parse_args()

    if args.subparser_name == "deploy":

        if not args.remotehost:
            print("Must specify remote host!")
            sys.exit(-1)

        if not args.appname:
            print("Must specify app name!")
            sys.exit(-1)

        env_vars = {}
        if args.environmentvariablesprefixedby:
            for name, value in os.environ.items():
                if name.startswith(args.environmentvariablesprefixedby):
                    env_vars[name[len(args.environmentvariablesprefixedby) :]] = value

        deploy = Deploy(
            directory=os.getcwd(),
            remote_user=args.remoteuser,
            remote_host=args.remotehost,
            remote_port=args.remoteport,
            app_name=args.appname,
            http_auth_user=args.httpauthuser,
            http_auth_password=args.httpauthpassword,
            environment_variables_json_string=args.environmentvariablesjson,
            environment_variables=env_vars,
            nginx_client_max_body_size=args.nginxclientmaxbodysize,
            nginx_proxy_read_timeout=args.nginxproxyreadtimeout,
            ps_scale=args.psscale,
            letsencrypt_email=args.letsencryptemail,
            letsencrypt_enable=bool(args.letsencryptemail),
        )
        deploy.go()

    elif args.subparser_name == "destroy":

        if not args.remotehost:
            print("Must specify remote host!")
            sys.exit(-1)

        if not args.appname:
            print("Must specify app name!")
            sys.exit(-1)

        destroy = Destroy(
            directory=os.getcwd(),
            remote_user=args.remoteuser,
            remote_host=args.remotehost,
            remote_port=args.remoteport,
            app_name=args.appname,
        )
        destroy.go()


if __name__ == "__main__":
    main()
