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

Pass a JSON block by `--environmentvariablesjson` or set the `DOKKUSD_ENVIRONMENT_VARIABLES_JSON` environmental variable.

Be careful to escape any fields:

.. code-block:: bash

    DOKKUSD_ENVIRONMENT_VARIABLES_JSON={\"ENV\":\"dev\",\"DATABASE\":\"dev\"} python -m dokkusd.cli deploy
