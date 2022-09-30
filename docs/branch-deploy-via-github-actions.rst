Branch Deploy via GitHub Actions
================================



Scenario: You want every branch except for the main branch to deploy to a Dokku server when created, to update itself and be deleted from the Dokku server when the branch is deleted.


For this you will need the dokkusd plugin installed on the server, see https://github.com/OpenDataServices/dokkusd-plugin


Make sure the app deploys to Dokku when running the dokkusd deploy command locally. If any resources are needed, this includes setting up an app.json and making sure resources are created too.


Create a SSH keypair on your local machine.


Take the public part, and on the dokku server run:

echo 'PUBLIC-KEY-CONTENTS' | dokku ssh-keys:add KEY-NAME

Make sure to give it a very clear name so other people know what the key is for.

Go to GitHub settings for the repository and add the following repository secrets:

DOKKUSD_BRANCH_APP_NAME_PREFIX: App name prefix. should be something unique on dokku server

DOKKUSD_BRANCH_SSH_PRIVATE_KEY: This is the contents of the private key you just created

DOKKUSD_BRANCH_SSH_KEYSCAN: The result of running ssh-keyscan against the Dokku server

DOKKUSD_BRANCH_REMOTE_HOST: The host name of the dokku server


Optinally, also set:

DOKKUSD_BRANCH_REMOTE_PORT: 

DOKKUSD_BRANCH_REMOTE_USER: 


Create the following Github actions files:


To create the branch, branch-deploy.yml

It's contents can be copied from https://github.com/OpenDataServices/dokkusd-test/blob/main/.github/workflows/branch-deploy.yml

To delete the branch, branch-destroy.yml

It's contents can be copied from https://github.com/OpenDataServices/dokkusd-test/blob/main/.github/workflows/branch-destroy.yml
