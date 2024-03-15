# WebBIP
Web application for Basic Image Processing (WebBIP)

## General Requirements for Local Installation

- python >= 3.8
- pip3
- virtualenv
- postgresql >= 12

### Virtual environment

Usually a virtual environment is used for each program or application of this project. In order to create a virtual environment the following commands can be used inside of app folders:

1. virtualenv .
2. source bin/activate

### PostgreSQL Database

In order to create a new database for WebBIP follow the next steps:

```bash
# Install and perform the necessary initial configuration in you system. Install the packages from the repositories by typing:

sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib

# Create the database for WebBIP :

sudo -u postgres psql

CREATE DATABASE webbip; 
CREATE USER admin WITH PASSWORD 'admin';

ALTER ROLE admin SUPERUSER;
ALTER ROLE admin SET client_encoding TO 'utf8';
ALTER ROLE admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE admin SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE webbip TO admin;

\q

# if you want to delete the database and create another database use:
DROP DATABASE webbip; 

# After deteting or "drop", create the database following the mentioned commands

```

Running the PostgreSQL server:

> sudo service postgresql start

### Get Start with WebBIP Locally

This folder contains a web application developed in Django.
In order to run the web server locally, a virtual environment is used as mentioned in section above.

### Requeriments

The requirements can be installed using the following command:

> pip install -r requirements.txt

### Running the WebBPI

Inside of the virtualenviroment the migration have to be done as follows:

```bash
python manage.py makemigrations
python manage.py migrate
```

If you want to access to the admin view of Django (/admin/), it needed to create a superuser account as follows:

```bash
python manage.py createsuperuser
```
Start running the WebBPI:

```bash
python manage.py runserver
```
