# Atlas
The Atlas API is an internal project management service for my personal and 8BitGhost projects. Most of the endpoints
are private but it does expose a small public API which is consumed by my portfolio website. It uses HTTP methods and 
a RESTful endpoint structure. The API authorization framework is OAuth. The current API version is beta.

## API Documentation
Visit the [api docs](http://django-rest-starter.herokuapp.com/)

## Table of Contents

- [Getting Started](#getting-started)
- [Development Environment](#development-environment)
    - [Install demo data](#install-demo-data)
- [Development](#development)
- [Release Process](#release-process)
- [Helpful Commands](#helpful-commands)

# Getting Started

The first step to start working on this project is to clone the repository onto your computer
```bash
$ git clone https://gitlab.com/alexolivas/atlas
```

Setup git flow, follow instructions and accept the defaults
```bash
$ git flow init
```
# Development Environment
This project is run inside a [docker](https://www.docker.com/)docker container. Running the development environment inside a docker container will resemble a production environment.

Navigate to the project inside your working directory (the place you cloned the project)
```bash
$ cd <repo-directory>/atlas
```

Create an environment variables file 
```bash
$ vi .env
```

Populate it with the following (generate the SECRET_KEY with a tool like 1password: 50 characters) environment variables. It is important that these variables exist so that the application can run
```
SECRET_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
DEBUG=True
DATABASE_URL='postgres://<db-user>:<db-user-password>@localhost:5432/<db-name>'
ALLOWED_HOSTS=[<your_host_url>]
CORS_ORIGIN_WHITELIST=<your_cors_hosts>
```

TODO: I still need to implement this postgres section!

Create an environment variables file for the postgres container
```bash
$ vi .postgres-env
```

Populate it with the following data, generate a new 15 character password specific to your environment
```
POSTGRES_USER: atlasuser
POSTGRES_PASSWORD: XXXXXXXXXXXXXXX
POSTGRES_DB: atlas_db
```

This project is setup to run inside docker. It consists of two images, the django project and the postgres database. Run the following command to build the project for the first time (or anytime you want to start fresh)
```bash
$ docker-compose up --build
```

## Install demo data

TODO: I need to figure this part out still. Something like installing demo data.

# Development
This project uses gitflow

## Start Feature
test

## Publish New Image
test

## Run Unit Tests
Add this section

## Update Demo Data
Test

# Release Process
TODO Add this


# Helpful Commands
Run this command to display the project's dependencies as a tree structure (pipdeptree comes pre-configured as a dependency on this project)
```bash
$ pipdeptree
```

Run this command to update any outdated pip dependencies. See this [blog](https://wakatime.com/blog/22-keeping-your-pip-requirements-fresh) for additional information
```bash
$ pur -r requirements.txt
```

## ---- DEPRECATED BELOW ----


## Everything below needs to be revised
The majority of this README file should be deprecated because it hasn't been revisited in a long time. I need to research how to setup and run a django rest project locally with minimal resources e.g. inside a docker container. I'm using the following instructions https://medium.com/backticks-tildes/how-to-dockerize-a-django-application-a42df0cb0a99 to dockerize this app

Create superuser
```
python manage.py createsuperuser --email admin@test.com
Default user:
admin
admin123
```

Create users and database instances
```psql
postgres=# CREATE USER postgres WITH SUPERUSER;
CREATE DATABASE <database-name>;
GRANT ALL PRIVILEGES ON DATABASE <database-name> TO postgres;
CREATE USER <db-user> WITH PASSWORD '<password>';
GRANT ALL PRIVILEGES ON DATABASE <database-name> TO <db-user>;
```

To run inside of a Docker container
```bash
docker-compose up -d --build --force-recreate
```

After the container has spinned up, "SSH" into the docker machine
```bash
bash -c "clear && docker exec -it atlas_starter_web_1 sh"
```

Once inside the docker machine, run the initial database migrations (not using a relational database, using SQLite)
```bash
python manage.py migrate
```

Finally, create a superuser, run the following command and follow the step by step instructions
```bash
python manage.py createsuperuser
```

## Virtualenv
[Virtualenv](https://pypi.python.org/pypi/virtualenv) is a python environment builder and is used together with [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/), which is a set of extensions to the original virtualenv tool.
Their primary purpose is to create isolated python environments, which is useful when working with multiple python projects that may have different dependencies.

### Pre Requisites

Install virtualenv
```bash
pip install virtualenv
```

Install virtualenvwrapper
```bash
pip install virtualenvwrapper
```

Create a directory to store details of your future virtual environments (this can be whatever location you'd like but remember it for the next step).
```bash
cd ~
mkdir .virtualenvs
mkdir Development/
```

Edit the bash profile (create it if it doesn't exist)
```bash
vi ~/.bash_profile
```

Add the following to your bash_profile
```
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Development
source /usr/local/bin/virtualenvwrapper.sh
```

Run the following command, if it installed correctly you will get a help menu
```bash
mkvirtualenv
```

Last step to be able to work with virtualenvwrapper and environment variables.
```bash
vi ~/.virtualenvs/postactivate
```

Add the following code snippet inside postactivate so that the project's environment variables are available on activate
```
set -a
. .env
set +a
```

### Create Virtual Environment

Create a virtual environment for this project
```bash
mkvirtualenv atlas
```

After running the command above, your environment is created and you should automatically be inside. You can verify that you are working inside your virtual environment if you bash shell looks like this:
```bash
(atlas)computername:current-directory username$
```

Within your virtual environment, install the project's requirements
```bash
pip install -r requirements.txt
```

Run the initial database migrations
```bash
python manage.py migrate
```

### Create Superuser
Run the following command and follow the step by step instructions
```bash
python manage.py createsuperuser
```

## Data
Once you have your local development environment running you will want to load your database with test data so that you can interact with the system.
Run the following (from the project's root directory):
```bash
cd /atlas/resources/
python refresh_db.py
```

Additionally if you want to backup your current database's state, run the following (from the project's root directory):
```bash
cd /atlas/resources/
python backup_db.py
```

# Wercker And Heroku Deployment
This project's demo is continuously built by [wercker](http://wercker.com/) and deployed by the push of a button to [heroku](http://heroku.com). I followed the [wercker deployments steps](http://devcenter.wercker.com/quickstarts/deployment/heroku.html) to get the app deployed.
