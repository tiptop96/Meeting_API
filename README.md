# Meeting_API

REST-api for a meeting database.

A backend with ability to create multiple accounts to auth'ed people and let them add meeting. These can later be fetched as json trough a url-queries.

When adding a meeting I the app asks google-places for corectley formatted adresses (street, city, country) always in english so that querying the database always is done in a uniform pattern.
