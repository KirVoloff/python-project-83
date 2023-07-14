### Hexlet tests, linter status and CI ::
[![Actions Status](https://github.com/KirVoloff/python-project-83/workflows/hexlet-check/badge.svg)](https://github.com/KirVoloff/python-project-83/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/30cfc7232ea9f0f66ffb/maintainability)](https://codeclimate.com/github/KirVoloff/python-project-83/maintainability)


https://page-analyzer-zsc3.onrender.com

# Getting started


### Description:

A web application that execute requests over the network and stores data in a database.


### Requirements:

* python 3.10
* Flask 2.3.2
* PostgreSQL 14.5
* Bootstrap 5.2.3


### Installation:

Use the package manager pip:

>    pip install --user git+https://github.com/KirVoloff/python-project-83.git

## Or

Clone repository and use poetry:

>    git clone https://github.com/KirVoloff/python-project-83git
>    cd python-project-83
>    make build
>    make install

1. Create PostgreSQL database with cheatsheet (database.sql)

2. Create .env file and add variables or add them straight into your environment with export

>    DATABASE_URL={provider}://{user}:{password}@{host}:{port}/{db}

>    SECRET_KEY='secret_key'

3. Run make dev for debugging (WSGI debug='True'), or make start for production (gunicorn)
