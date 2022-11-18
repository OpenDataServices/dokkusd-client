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

You can set these via `app.json`:

.. code-block:: json

    {
        "dokkusd": {
            "environment_variables": {
                "cat":"lucky",
                "human": "bob"
            }
        }
    }

You can also set these on the command line - see the deploy call.


Keep Git Dir
------------

https://dokku.com/docs/deployment/methods/git/#keeping-the-git-directory

You can set this via `app.json`:

.. code-block:: json

    {
        "dokkusd": {
            "keep_git_dir": True
        }
    }


HTTP Auth with user and password
--------------------------------

Currently this can only be set on the command line - see the deploy call.

Commands
--------

You can specify Dokku commands to be run on deploy time.

.. code-block:: json

    {
        "dokkusd": {
            "commands": [
                ["nginx:set","$APP_NAME","client-max-body-size","50m"]
            ]
        }
    }

Commands must have "$APP_NAME" in, or they won't be run - for security reasons.

Be careful with other elements that look like variable names, as in the future they might be. eg "$SIZE"
