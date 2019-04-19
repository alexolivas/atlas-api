# Atlas
The Atlas API is an internal project management service for my personal and 8BitGhost projects. Most of the endpoints
are private but it does expose a small public API which is consumed by my portfolio website. It uses HTTP methods and 
a RESTful endpoint structure. The API authorization framework is OAuth. The current API version is beta.

## Table of Contents
- [API Docs](#api-docs)
- [Get Key](#get-key)
- [Development](#development)
    - [Getting Started](#getting-started)
    - [Setup Environment](#setup-environment)
    - [Install Data](#install-data)
    - [Start Feature](#start-feature)
    - [Publishing Images](#publishing-images)
    - [Running Tests](#runing-tests)
    - [Demo Data](#demo-data)
        - [Examples](#Examples)
    - [Starting a container](#starting-a-container)
    - [Helpful Commands](#helpful-commands)
- [Release Process](#release-process)
    - [Heroku Setup](#heroku-setup)

## API Documentation
Visit the [api docs](http://django-rest-starter.herokuapp.com/)

## Get Key
Add this section on obtaining a key to use this service with a couple examples.

## Development
This project uses gitflow and runs inside a docker container.

### Getting Started
The first step to start working on this project is to clone the repository onto your computer
```bash
$ git clone https://gitlab.com/alexolivas/atlas
```

Setup git flow, follow instructions and accept the defaults
```bash
$ git flow init
```
### Setup Environment
This service is run inside a [docker](https://www.docker.com/)docker container to resemble a production environment. To get started, navigate to the repo (the directory where you cloned the project)
```bash
$ cd <repo-directory>/atlas
```

Create an environment variables file at the root for the postgres container
```bash
$ vi .postgres-env
```

Populate it with the following data, generate a new 15 character password specific to your environment. Note these values will be required to generate the DATABASE_URL in the next step
```
POSTGRES_USER: atlasuser
POSTGRES_PASSWORD: XXXXXXXXXXXXXXX
POSTGRES_DB: atlas_db
```

Create a second environment variables file at the root for the django application
```bash
$ vi .env
```

Populate it with the following environment variables, generate the SECRET_KEY with a tool like 1password: 50 characters. It is important that these variables exist so that the application can run.
NOTE: The ALLOWED_HOSTS variable must be a comma separated lists if there are multiple hosts e.g. 'localhost', '127.0.0.1' 
```
ENVIRONMENT=development
SECRET_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
DEBUG=True
DATABASE_URL=postgres://<POSTGRES_USER>:<POSTGRES_PASSWORD>@atlas-db:5432/<POSTGRES_DB>
ALLOWED_HOSTS=localhost, 127.0.0.1
CORS_ORIGIN_WHITELIST='localhost:3000', '127.0.0.1:3000'
```

Optionally, if you want to setup the photo upload feature you will have to setup an [s3 bucket](https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html) 
and add the following environment variables in your .env file once you've set it up
```
AWS_S3_ACCESS_KEY_ID=XXXXX
AWS_S3_SECRET_ACCESS_KEY=XXXXX
AWS_STORAGE_BUCKET_NAME=XXXXX
```

Again, optionally, if you want to setup the contact me feature you must add the following environment variable with the email address you want to receive your emails
```
DEFAULT_CONTACT_EMAIL_ADDRESS=<email-address>
```

This project is setup to run inside docker. It consists of two images, the django project and the postgres database. Run the following command to build the project for the first time (or anytime you want to start fresh)
```bash
$ docker-compose up --build
```

### Install Data

Once you have your local development environment running you will want to load your database with demo data so that you can interact with the system.
Run the following (from the project's root directory):
```bash
$ python restore_db.py
```

Once the demo data is installed on your system you can login to the admin portal at localhost:8000/admin with the credentials admin/admin123

### Start Feature
```bash
$ git flow feature start $FEATURE_NAME
```

### Publishing Images
When a new version of the atlas API is ready to be released, run the following command to publish the latest version up to docker hub
```bash
$ docker push alexolivas/atlas_api:latest
```

### Running Tests
```bash
$ python manage.py test
```

### Demo Data
From time to time its possible that I may want to add data for a particular feature and make it available to the project's demo data. This section provides a step by step guide for how to achieve this.

To create a backup of the current state of your database (specific to an APP) run the following command
```bash
$ python manage.py dumpdata $DJANGO_APP > $BACKUP_FILE.json
```

Then move the resulting backup to the resources directory
```bash
$ mv web.json resources/demo-data/$BACKUP_FILE.json
```

### Starting a container
To rebuild the container entirely run the following command
```bash
docker-compose up --build
```

To start a container
```bash
docker-compose up
```

#### Examples
The following are examples of the primary applications whose data will be periodically updated to a state where we would want to create a backup

The web app contains all the information used by the portfolio website
```bash
$ python manage.py dumpdata web > resources/demo-data/web.json
```

The accounts app contains all the client accounts
```bash
$ python manage.py dumpdata accounts > resources/demo-data/accounts.json
```

The projects app contains all the projects in my portfolio
```bash
$ python manage.py dumpdata projects > resources/demo-data/projects.json
```

The auth.user app is the out of the box django app containing users that can login to the admin portal. This should already have 1 admin account but its possible that in the future I may add a feature that could require a different user
```bash
$ python manage.py dumpdata auth.user > resources/demo-data/users.json
$ python manage.py dumpdata auth.group > resources/demo-data/user-groups.json
```

The user's tokens are also out of the box
```bash
python manage.py dumpdata authtoken > resources/demo-data/tokens.json
```

### Helpful Commands
Run this command to display the project's dependencies as a tree structure (pipdeptree comes pre-configured as a dependency on this project)
```bash
$ pipdeptree
```

Run this command to update any outdated pip dependencies. See this [blog](https://wakatime.com/blog/22-keeping-your-pip-requirements-fresh) for additional information
```bash
$ pur -r requirements.txt
```

## Release Process
To setup bitbucket pipelines you have to add the following pipeline environment variables

| Environment Variable  | Value                                                |
| ----------------------| -----------------------------------------------------|
| ENVIRONMENT           | <development/stage/production>                       |
| DATABASE_URL          | sqlite:////atlas-db.sqlite                           |
| CORS_ORIGIN_WHITELIST | '<website-url>'                                      |
| DEBUG                 | True/False                                           |
| ALLOWED_HOSTS         | <hostname>                                           |
| SECRET_KEY            | XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX |
| DEFAULT_CONTACT_EMAIL_ADDRESS | <email-address>                              |
| DISABLE_COLLECTSTATIC | 1                                                    |

Merging a feature branch into develop automatically triggers the build pipeline to run unit tests to verify that the feature doesn't break anything on develop and deploys a new development environment to Heroku.

To schedule a release, use gitflow to create a release branch. Pushing up changes to a release branch automatically triggers the build pipeline to run unit tests and deploy a new staging RC environment to Heroku.
NOTE: when starting a new release I have to manually (for now) update the version in atlas.__version__. To determine the next version use the following commands:

next patch: 1.4.2 -> 1.4.3
```bash
$ VERSION=`git semver --next-patch`
```
next minor: 1.4.2 -> 1.5.0
```bash
$ VERSION=`git semver --next-minor`
```
next major: 1.4.2 -> 2.0.0
```bash
$ VERSION=`git semver --next-major`
```

The above was taken from: https://romain.dorgueil.net/blog/en/tips/2016/08/20/releases-with-git-semver.html

Merging into master triggers the build pipeline:
- run the unit tests 
- if they pass, tag the release to the next version (maybe)
- deploy to heroku (stage environment to keep environments in sync)
- promotes stage to production

### Heroku Setup
Production and staging environments are hosted on Heroku. In order to get this REST API to run correctly we must setup the same environment variables we setup for development. However, with different values for each environment.