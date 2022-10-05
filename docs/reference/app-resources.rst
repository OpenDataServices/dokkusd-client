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

Items in the volumes array can be a string or a dict.

If a string, it should be the location in the container you want the storage mounted at. You can only have one string in the list.

If a dict, it should be:

.. code-block:: json

    {
        "dokkusd": {
            "volumes": [
                {"host_subdir": "database", "container_path": "/database"}
            ]
        }
    }

* `host_subdir`: The sub directory on the host that will be used. The app name will be put in front.
* `container_path`: The location in the container you want the storage mounted at

You can have as many dict's as you want in the list and in this way, define multiple storage volumes. `host_subdir` should be unique.

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

Environment Variables
---------------------

.. code-block:: json

    {
        "dokkusd": {
            "environment_variables": {
                "cat":"lucky",
                "human": "bob"
            }
        }
    }


HTTP Auth with user and password
--------------------------------

Currently this can only be set on the command line - see the deploy call.
