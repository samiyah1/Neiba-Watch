### NEIGHBOURHOOD
## Neighbourhood Watch
## Description

This is an application where users can sign in and get the latest neighbourhood notices and businesses around the neighbourhood . Users can join neighbourhood to the post Notices.
Link to deployed site

https://neiba-watch.herokuapp.com
## Table of content

    * Description
    * Setup and installations
    * Deployment
    * Contributing
    * Bugs
    * Contact me
    * Licensing

## Setup and installations
Prerequisites

    Python3.6
    Postgres
    virtualenv
    Pip

Technologies used

- Python 3.6
- HTML
- Bootstrap 4
- Heroku
- Postgresql

Clone the Repo and checkout into the project folder.

https://github.com/samiyah1/Neiba-Watch.git

Create and activate the virtual environment

python3.6 -m virtualenv virtual

source virtual/bin/activate

Setting up environment variables

Create a .env file and paste paste the following filling where appropriate:

SECRET_KEY='<Secret_key>'
DBNAME='watch'
USER='<Username>'
PASSWORD='<password>'
DEBUG=True

EMAIL_USE_TLS=True
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER='<your-email>'
EMAIL_HOST_PASSWORD='<your-password>'

Install dependancies

Install dependancies that will create an environment for the app to run pip install -r requirements.txt
Create the Database

In a new terminal, open the postgresql shell with psql.

CREATE DATABASE watch;

Make and run migrations

python3.6 manage.py makemigrations && python3.6 manage.py migrate

Run the app

python3.6 manage.py runserver

Open localhost:8000
Deployment

To deploy the application, please follow the instructions in this gist
Contributing

Please read this comprehensive guide on how to contribute. Pull requests are welcome :-)
Bugs

Create an issue mentioning the bug you have found
Known bugs

    cannot subscribe to email list in live application

Support and contact details

Contact Mariam Omar for further help/support
License

MIT

Copyright (c)2018  Mariam Omar
