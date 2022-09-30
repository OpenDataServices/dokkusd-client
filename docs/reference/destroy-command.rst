Destroy Command
===============


The destroy command deletes the app on the dokku server, along with any specified resources. Note this can be very dangerous!


Call
----

.. code-block:: bash

    python -m dokkusd.cli destroy --help


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
