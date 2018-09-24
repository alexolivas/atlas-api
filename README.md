# Atlas
The Atlas API is an internal project management service for my personal and 8BitGhost projects. Most of the endpoints
are private but it does expose a small public API which is consumed by my portfolio website. It uses HTTP methods and 
a RESTful endpoint structure. The API authorization framework is OAuth. The current API version is beta.

## Everything below needs to be revised
The majority of this README file should be deprecated because it hasn't been revisited in a long time. I need to research how to setup and run a django rest project locally with minimal resources e.g. inside a docker container.

Visit the [api docs](http://django-rest-starter.herokuapp.com/)

[![build status](https://gitlab.com/alexolivas/atlas/badges/master/build.svg)](https://gitlab.com/alexolivas/atlas/commits/master)
[![coverage report](https://gitlab.com/alexolivas/atlas/badges/master/coverage.svg)](https://gitlab.com/alexolivas/atlas/commits/master)
[![Dependency Status](https://gemnasium.com/alexolivas/django-rest-starter.svg)](https://gemnasium.com/alexolivas/django-rest-starter)


## Table of Contents

- [Getting Started](#getting-started)
- [Running Locally](#running-locally)
    - [Database Setup](#database-setup)
    - [Docker](#docker)
    - [Virtualenv](#virtualenv)
        - [Pre Requisites](#pre-requisites)
        - [Create Virtual Environment](#create-virtual-environment)
        - [Create Superuser](#create-superuser)
    - [Data](#data)
- [Helpful Commands](#helpful-commands)
- [Wercker/Heroku Deployment](#wercker-and-heroku-deployment)

-------
# Getting Started
- The first step to start working on this project is to fork the repository into your personal github account.
- Next, clone the forked repository into your local environment

```bash
git clone https://gitlab.com/alexolivas/atlas
```

For updating your fork from the remote (upstream)
```bash
git remote add upstream https://gitlab.com/alexolivas/atlas
```

Make sure upstream is configured as expected, should see origin for fork and upstream to main repo
```bash
git remote -v
```

Create an environment variables file
```bash
vi .env
```

Populate it with the following (generate the SECRET_KEY with a tool like 1password: 50 characters)
```
SECRET_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
DEBUG=True
DATABASE_URL='postgres://<db-user>@localhost:5432/<db_name>'
ALLOWED_HOSTS=<your_host_url>
CORS_ORIGIN_WHITELIST=<your_cors_hosts>
DATA_REFRESH=<TRUE OR FALSE - Do not use in production>
```


# Running Locally
You can either run the project inside a [docker](#docker) container or inside a [virtual environment](#virtualenv). If you are actively developing on a local copy of django-rest-starter it is recommended that you use a virtual environment.
With a virtual environment you have the benefit of making changes without having to redeploy or start up the web server each time. You can do the same with docker but you have to setup port forwarding.

## Database Setup
During the development phase I typically use a postgres database to simulate production as much as possible. These are the database setup instructions I use for my django and django-rest projects.

Install postgres if it is not already in your system
```bash
brew install postgresql
```

PSQL into postgres
```bash
psql postgres
```

Create users and database instances
```psql
postgres=# CREATE USER postgres WITH SUPERUSER;
CREATE DATABASE <database-name>;
GRANT ALL PRIVILEGES ON DATABASE <database-name> TO postgres;
CREATE USER <db-user> WITH PASSWORD '<password>';
GRANT ALL PRIVILEGES ON DATABASE <database-name> TO <db-user>;
```

## Docker
[Docker](https://www.docker.com/) is an open platform for developers and sysadmins to build, ship, and run distributed applications whether on laptops, data center VMs, or the cloud. 
Running your local environment inside a docker container will resemble a production environment.

NOTE: Docker usage is still a work in progress, I still need to create the docker files and another docker container for postgres.

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

# Helpful Commands
Run this command to display the project's dependencies as a tree structure (pipdeptree comes pre-configured as a dependency on this project)
```bash
pipdeptree
```

# Wercker And Heroku Deployment
This project's demo is continuously built by [wercker](http://wercker.com/) and deployed by the push of a button to [heroku](http://heroku.com). I followed the [wercker deployments steps](http://devcenter.wercker.com/quickstarts/deployment/heroku.html) to get the app deployed.
