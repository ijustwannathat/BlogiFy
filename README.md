# This website was influenced by the book.
* [Django 4 by Example](https://www.amazon.com/Django-Example-powerful-reliable-applications/dp/1801813051)
### I'm very thankful for material this books provides
## General material:
This website introduces us to a basic logic django blog application with user authorisation and drf included.
# Part one. Setting db and dependencies
___
## Setting up
```shell
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt   
```
## Managing db.
Note: 
* You need to create your own postgres database in order for it to work using
```shell
$ CREATE USER blog WITH PASSWORD '<password>'; #set a password
$ CREATE DATABASE blog OWNER blog ENCODING 'UTF8';
```
### move bellow and fill the necessary fields with information regarding your database
___
## Move on if you did the steps, otherwise try adding you own data! 
* First of all you need to create db
```shell
$ python manage.py makemigrations
$ python manage.py migrate
```
* You need to either load your own data later via admin or 
load them from preinstalled in the project json file [mysite_json.data](mysite_data.json)
```shell
$ python -Xutf8 manage.py loaddata mysite_data.json
```
### Quick note: Default password and login for admin panel from loaded data are
* login: admin
* password: admin

#### In case those don't work i suggest that you create your own superuser via terminal
```shell
$ python manage.py createsuperuser
```
---
# Part two. Setting variables(Optional)
___
* If you want to check how email recommendation works you need to create your own .env file
```shell
$ touch .env
```
* Follow all steps here [click](https://support.google.com/accounts/answer/185833) and get 16-digit code
```shell
EMAIL_HOST = '' #your email from which you're going to send recommendations
EMAIL_PASSWORD = '' #your 16-digit code
```
---
# All ready. Last step is to run application
```shell
$ python manage.py runserver
```
___
## .env file structure 
* GitHub authorisation can be done by [click](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github)
* And following Google authorisation [Click me!](https://medium.com/analytics-vidhya/adding-sign-in-with-google-to-your-website-b82755b79b31)

```python
EMAIL_HOST = ''
EMAIL_PASSWORD = ''
DB_PASSWORD = ''
GITHUB_CLIENT_ID=''
GITHUB_SECRET_KEY=''
GOOGLE_CLIENT_ID=''
GOOGLE_SECRET_KEY=''
```


___
# If the website doesn't work you can write to <a href="mailto:kokfbc@gmail.com">kokfbc@gmail.com</a>

# Thank you!
