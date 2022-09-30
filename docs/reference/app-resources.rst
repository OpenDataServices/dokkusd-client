App Resources
=============

An App can specify that certain resources should be attached to it.

The file `app.json` should exist in the root of the repository.

Storage
-------

.. code-block:: json

    {
        "dokkusd": {
            "volumes": [
                "/usr/share/nginx/html/storage"
            ]
        }
    }

Currently the `volumes` array can only have one item.

This should be a string of the location inside the container you want the storage to be available at.

Services
--------

.. code-block:: json

    {
        "dokkusd": {
            "services": [
                "postgres"
            ]
        }
    }

You can list the types of services you want attached to your app.

Currently each type can only be attached once.

HTTP Auth with user and password
--------------------------------

Currently this can only be set on the command line - see the deploy call.

