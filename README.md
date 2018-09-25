# Atlas
The Atlas API is an internal project management service for my personal and 8BitGhost projects. Most of the endpoints
are private but it does expose a small public API which is consumed by my portfolio website. It uses HTTP methods and 
a RESTful endpoint structure. The API authorization framework is OAuth. The current API version is beta.

## Table of Contents
- [API Docs](#api-docs)
- [Getting Started](#getting-started)
- [Development Environment](#development-environment)
    - [Install Data](#install-data)
- [Development](#development)
    - [Start Feature](#start-feature)
    - [Publishing Images](#publishing-images)
    - [Running Tests](#runing-tests)
    - [Demo Data](#demo-data)
        - [Examples](#Examples)
- [Release Process](#release-process)
- [Helpful Commands](#helpful-commands)

## API Documentation
Visit the [api docs](http://django-rest-starter.herokuapp.com/)

## Getting Started
The first step to start working on this project is to clone the repository onto your computer
```bash
$ git clone https://gitlab.com/alexolivas/atlas
```

Setup git flow, follow instructions and accept the defaults
```bash
$ git flow init
```
## Development Environment
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
```
SECRET_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
DEBUG=True
DATABASE_URL='postgres://<POSTGRES_USER>:<POSTGRES_PASSWORD>@localhost:5432/<POSTGRES_DB>'
ALLOWED_HOSTS=['*']
CORS_ORIGIN_WHITELIST='*'
```

This project is setup to run inside docker. It consists of two images, the django project and the postgres database. Run the following command to build the project for the first time (or anytime you want to start fresh)
```bash
$ docker-compose up --build
```

### Install Data

Once you have your local development environment running you will want to load your database with demo data so that you can interact with the system.
Run the following (from the project's root directory):
```bash
$ cd /atlas/resources/
$ python restore_db.py
```

## Development
This project uses gitflow

### Start Feature
test

### Publishing Images
When a new version of the atlas API is ready to be released, run the following command to publish the latest version up to docker hub
```bash
$ docker push alexolivas/atlas_api:latest
```

### Running Tests
Add this section

### Demo Data
From time to time its possible that I may want to add data for a particular feature and make it available to the project's demo data. This section provides a step by step guide for how to achieve this.

To create a backup of the current state of your database (specific to an APP) run the following command
```bash
$ python manage.py dumpdata $DJANGO_APP > $BACKUP_FILE.json
```

Then move the resulting backup to the resources directory
```bash
$ mv web.json atlas/resources/data/$BACKUP_FILE.json
```

#### Examples
The following are examples of the primary applications whose data will be periodically updated to a state where we would want to create a backup

The web app contains all the information used by the portfolio website
```bash
$ python manage.py dumpdata web > web.json
$ mv web.json atlas/resources/data/web.json
```

The accounts app contains all the client accounts
```bash
$ python manage.py dumpdata accounts > accounts.json
$ mv web.json atlas/resources/data/accounts.json
```

The projects app contains all the projects in my portfolio
```bash
$ python manage.py dumpdata projects > projects.json
$ mv web.json atlas/resources/data/projects.json
```

The auth.user app is the out of the box django app containing users that can login to the admin portal. This should already have 1 admin account but its possible that in the future I may add a feature that could require a different user
```bash
$ python manage.py dumpdata auth.user > users.json
$ mv web.json atlas/resources/data/users.json
```


## Release Process
TODO Add this


## Helpful Commands
Run this command to display the project's dependencies as a tree structure (pipdeptree comes pre-configured as a dependency on this project)
```bash
$ pipdeptree
```

Run this command to update any outdated pip dependencies. See this [blog](https://wakatime.com/blog/22-keeping-your-pip-requirements-fresh) for additional information
```bash
$ pur -r requirements.txt
```
