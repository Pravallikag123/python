#VideoApp
#Uploading and playing a VideoFile
#Step 1: Activate the Virtual Environment

C:\djangoapps2\myvenv\Scripts>.\activate

(myvenv) C:\djangoapps2\myvenv\Scripts>cd..

(myvenv) C:\djangoapps2\myvenv>cd..
#----------------------------------------------------------------------------------------------
#step 2: Creating a Project
(myvenv) C:\djangoapps2>django-admin startproject myproj33

(myvenv) C:\djangoapps2>cd myproj33

#---------------------------------------------------------------------------------------------
#Step 3: Creating an Application
(myvenv) C:\djangoapps2\myproj33>py manage.py startapp VideoApp

#--------------------------------------------------------------------------------------------
#step 4: Settings.py , adding application to settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'VideoApp'
]
#---------------------------------------------------------------------------------------------------
#step 5:
#goto chrome--------->say "django embed video
------>django embed video pypi------>pip install django-embed-video

(myvenv) C:\djangoapps2\myproj33>pip install django-embed-video


click the documentation------------>django embed video---->
withinthin the documentation----->click installation -->
and follow the installation steps

#-----------------------------------------------------------------------------------------------
#step 6:

#Add 'embed_video' to installed apps


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'VideoApp',
    'embed_video'
]

#----------------------------------------------------------------------------------------------
#step 7: Models.py

#In the documentation----->click next ----->goto model ecamples---->copy the following
#and paste in Models.py

from django.db import models
from embed_video.fields import EmbedVideoField

class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()

#---------------------------------------------------------------------------------------------
#step 8:admin.py

#in documentation -------->copy the code within ----->Admin mixin examples   
from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Item

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)
#----------------------------------------------------------------------------------------------
#step 9: views.py

from django.shortcuts import render
from .models import Item
# Create your views here.
def input(request):
    obj=Item.objects.all()
    return render(request,'base.html',{'obj':obj})

#---------------------------------------------------------------------------------------------
#step 10: base.html

create---->templates folder---->create base.html file

Goto-->getbootstrap.com---->all releases--->select version 4.5---->
copy starter template and paste in base.html

in django embed documentation ------->Goto templates examples---->copy the tag---->
{% load embed_video_tags %}

add this to base.html

and within the body change the code as


{% load embed_video_tags %}
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <h1>VIDEO WORLD!</h1>
    {% for p in obj%}
    {% video p.video 'small' %}
    {% endfor %}

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: jQuery and Bootstrap Bundle (includes Popper) -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>

    <!-- Option 2: jQuery, Popper.js, and Bootstrap JS
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js" integrity="sha384-w1Q4orYjBQndcko6MimVbzY0tgp4pWB4lZ7lr30WKz0vr/aWKhXdBNmNb5D92v7s" crossorigin="anonymous"></script>
    -->
  </body>
</html>

#---------------------------------------------------------------------------------------------
#step 11: goto settings.py and add Template folder

import os

TEMPLATE_DIR=os.path.join(BASE_DIR,'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
#-----------------------------------------------------------------------------------------------
#step 12: Application urls.py

from django.urls import re_path
from VideoApp import views
urlpatterns=[
     re_path('',views.input)
]

#----------------------------------------------------------------------------------------------
#step 13:project urls.py

from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
urlpatterns = [
    path('admin/', admin.site.urls),
    url('',include('VideoApp.urls'))
]

#--------------------------------------------------------------------------------------------
#step 14: makemigrations

(myvenv) C:\djangoapps2\myproj33>py manage.py makemigrations
Migrations for 'VideoApp':
  VideoApp\migrations\0001_initial.py
    - Create model Item
#---------------------------------------------------------------------------------------------
#step 15: migrate
(myvenv) C:\djangoapps2\myproj33>py manage.py migrate

#---------------------------------------------------------------------------------------------
#step 16: create superuser

(myvenv) C:\djangoapps2\myproj33>py manage.py createsuperuser
Username (leave blank to use 'dell'): vijay
Email address: vijaysundertrainings@gmail.com
Password:
Password (again):
Superuser created successfully.

#--------------------------------------------------------------------------------------------
#step 17:runserver:

(myvenv) C:\djangoapps2\myproj33>py manage.py runserver
#------------------------------------------------------------------------------------------
#step 18: open admin interface:
http://127.0.0.1:8000/admin
provide username and password

open admin interface---->add item--------->add a video url from youtube---->save

give a request:
#http://127.0.0.1:8000
we can play the video here

#----------------------------------------------------------------------------------------------







        





        












































