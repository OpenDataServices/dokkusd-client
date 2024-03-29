Deploy Command
==============


The deploy command creates the app on the dokku server, along with any specified resources.


Call
----

.. code-block:: bash

    python -m dokkusd.cli deploy --help


Parameters for SSH connection
-----------------------------

Remote Host
~~~~~~~~~~~

Required.

Pass by `--remotehost` or set the `DOKKUSD_REMOTE_HOST` environmental variable.

Remote User
~~~~~~~~~~~

Optional.

Pass by `--remoteuser` or set the `DOKKUSD_REMOTE_USER` environmental variable.

Remote Port
~~~~~~~~~~~

Optional.

Pass by `--remoteport` or set the `DOKKUSD_REMOTE_PORT` environmental variable.

Parameters for App
------------------

App name
~~~~~~~~

Required.

Pass by `--appname` or set the `DOKKUSD_APP_NAME` environmental variable.

HTTP Auth user and password
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Optional, but both user and password are required if used.

Pass the user by `--httpauthuser` or set the `DOKKUSD_HTTP_AUTH_USER` environmental variable.

Pass the password by `--httpauthpassword` or set the `DOKKUSD_HTTP_AUTH_PASSWORD` environmental variable.

Environment Variables
~~~~~~~~~~~~~~~~~~~~~

Optional.

Pass a string `--environmentvariablesprefixedby`. Any Environmental variables that start with this will be used.

eg.

.. code-block:: bash

    THESE_VARS_TEST_1=cats python -m dokkusd.cli deploy --environmentvariablesprefixedby THESE_VARS_

Will result in TEST_1=cats being set on the Dokku app.


Pass a JSON block by `--environmentvariablesjson` or set the `DOKKUSD_ENVIRONMENT_VARIABLES_JSON` environmental variable.

Be careful to escape any fields:

.. code-block:: bash

    DOKKUSD_ENVIRONMENT_VARIABLES_JSON={\"ENV\":\"dev\",\"DATABASE\":\"dev\"} python -m dokkusd.cli deploy

Nginx Client Max body size
~~~~~~~~~~~~~~~~~~~~~~~~~~

Sets the Nginx Client Max body size.

Pass a string to `--nginxclientmaxbodysize` or set the `DOKKUSD_NGINX_CLIENT_MAX_BODY_SIZE` environmental variable.

Should include units. eg `50m` not `50`.

Nginx Proxy Read Timeout
~~~~~~~~~~~~~~~~~~~~~~~~

Sets the Nginx Proxy Read Timeout.

Pass a string to `--nginxproxyreadtimeout` or set the `DOKKUSD_NGINX_PROXY_READ_TIMEOUT` environmental variable.

Should include units. eg `120s` not `120`.

Scale Processes
~~~~~~~~~~~~~~~

Sets the ps:scale command, to set the number of each different type of process types to run.

Pass a string to `--psscale` or set the `DOKKUSD_PS_SCALE` environmental variable.

Lets Encrypt
~~~~~~~~~~~~

Enables Lets Encrypt HTTPS. You must set the email address for the Lets Encrypt account to use this.

Pass a string to `--letsencryptemail` or set the `DOKKUSD_LETSENCRYPT_EMAIL` environmental variable.
