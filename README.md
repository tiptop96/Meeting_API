# Meeting_API

REST-api for a meeting database.

A backend with ability to create multiple accounts to auth'ed people and let them add meeting. These can later be fetched as json trough a url-queries.

When adding a meeting I the app asks google-places for corectley formatted adresses (street, city, country) always in english so that querying the database always is done in a uniform pattern.

## Installation and Getting Go

```
$ sudo apt-get install python3-pip
$ sudo pip3 install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip3 install django
$ pip3 install djangorestframework
$ pip3 install django psycopg2
```

Add your localhost IP or host to MeetingAPI/settings.py in ALLOWED_HOSTS.

`$ python manage.py runserver`

💥 🔥
