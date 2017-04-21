# STATUS

[![Build Status](https://travis-ci.org/reginaldojunior/api-django.svg?branch=master)](https://travis-ci.org/reginaldojunior/api-django)

[![Coverage Status](https://coveralls.io/repos/github/reginaldojunior/api-django/badge.svg?branch=master)](https://coveralls.io/github/reginaldojunior/api-django?branch=master)

# INSTALL

### First init virtual env with this steps

 - sudo pip install virtualenv
 - virtualenv --no-site-packages projetos
 - cd /projetos/
 - git clone https://github.com/reginaldojunior/api-django.git
 - run dependencies pip "pip install -r requirements.txt"
 - configure database on path /projetos/api-django/settings.py
 - run migrate "python manager.py makemigrations"
 - run migrate tables "python manager.py migrate"

### Create User Admin
 
 - python manage.py shell

 - from django.contrib.auth.models import User
 - user=User.objects.create_user('foo', password='bar')
 - user.is_superuser=True
 - user.is_staff=True
 - user.save()

### Run Project

 - run server "python manager.py runserver"

### Routes 

 - host:port/docs/
 - host:port/api/
 - host:port/admin/
 - host:port/
