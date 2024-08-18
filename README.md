# Part one. Setting db and dependencies
## This website was influenced by the book.
* [Django 4 by Example](https://www.amazon.com/Django-Example-powerful-reliable-applications/dp/1801813051)
### I'm very thankful for material this books provides
## General material:
This website introduces us to a basic logic django blog application with user authorisation and drf included.

## Setting up
```
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt   
```
## Managing db.
* First of all you need to create db
```
$ python manage.py makemigrations
$ python manage.py migrate
```
* You need to either load your own data later via admin or 
load them from preinstalled in the project json file [mysite_json.data](mysite_data.json)
```
$ python -Xutf8 manage.py loaddata mysite_data.json
```
### Quick note: Default password and login for admin panel from loaded data are
* login: admin
* password: kokfbc

#### In case those don't work i suggest that you create your own superuser via terminal
```
$ python manage.py createsuperuser
```
---
# Part two. Setting variables(Optional)
* If you want to check how email recommendation works you need to create your own .env file
```
$ touch .env
```
* Follow all steps here [click](https://support.google.com/accounts/answer/185833) and get 16-digit code
```text
EMAIL_HOST = '' #your email from which you're going to send recommendations
EMAIL_PASSWORD = '' your 16-digit code
```
---
# All ready. Last step is to run application
```
$ python manage.py runserver
```
___
# If the website doesn't work you can write to <a href="mailto:kokfbc@gmail.com">kokfbc@gmail.com</a>

## Thank you!
