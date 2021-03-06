# Meeting_API

REST-api for a meeting database.

A backend with ability to create multiple accounts to auth'ed people and let them add meeting. These can later be fetched as json trough a url-queries.

When adding a meeting I the app asks google-places for corectley formatted adresses (street, city, country) always in english so that querying the database always is done in a uniform pattern.

## Installation

```
$ sudo apt-get install python3-pip
$ sudo pip3 install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip3 install django
$ pip3 install djangorestframework
$ pip3 install django psycopg2
```

## Getting Going

1. Setup and configure Postgres on your machine. [Tutorial](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04)
2. Create the following environment variables: `CA_API_DB, CA_API_USER, CA_API_PW, CA_API_HOST` and populate them with your database configuration.
    ```
    $ python manage.py makemigrations
    $ python manage.py migrate --database=pq
    ```
3. Add your localhost IP or host to MeetingAPI/settings.py in ALLOWED_HOSTS.
4. Run `$ python manage.py runserver`

💥 🔥
