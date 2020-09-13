# Django Blog Demo

## About

This is a test work.

It was made using **Python 3.8** + **Django==2.1.5** and database is **SQLite**.

## Prerequisites

Install virtual environment:

```bash
$ python3 -m venv env
```

Activate virtual environment:

On Linux:
```bash
$ source env/bin/activate
```

```bash
$ git clone https://github.com/Serdiuk-Roman/vf.git
```

```bash
$ cd vf
```

Install dependencies:
```bash
$ pip install -r requirements.txt
```

## How to run

### Default

You can run the application from the command line with manage.py.
Go to the root folder of the application.

Create migrations:
```bash
$ python manage.py makemigrations
```

Run migrations:
```bash
$ python manage.py migrate
```

```bash
$ python manage.py createsuperuser
```

For WhiteNoise:
```bash
$ python manage.py collectstatic
```

Run server:
```bash
$ python manage.py runserver
```


[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

or

[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)


After each additional image, you need to restart the server
