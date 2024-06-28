
#Develop a Django Project to accept Student details and print them

    STUDENT DETAILS

NAME:...............
ROLLNO:.............
Branch:.............
College:............
Enter marks of Maths :
Enter marks of Physics:
Enter marks of Chemistry:
        SUBMIT  RESET

#Process :  Browser---->give req--------->urls.py(project)----->urls.py(Application)(empty)--->
#           views(input)------>base.html(templates)----->Submit form---->urls.py(Application)
#--------->views(compute)----->displays  all details  and computing tot and avg and gives
#         response
Project Name: myproj7
Application Name:StudentApp


#Step 1: Activate Virtual Environment
C:\Users\DELL>cd\

C:\>cd djangoapps\myvenev\scripts
The system cannot find the path specified.

C:\>cd djangoapps\myvenv\scripts

C:\Djangoapps\myvenv\Scripts>.\activate

(myvenv) C:\Djangoapps\myvenv\Scripts>cd..

(myvenv) C:\Djangoapps\myvenv>cd..
#---------------------------------------------------------------------------------------------
#Step 2:Creating or starting a project
(myvenv) C:\Djangoapps>django-admin startproject myproj7

(myvenv) C:\Djangoapps>cd myproj7

(myvenv) C:\Djangoapps\myproj7>

#---------------------------------------------------------------------------------------------
#step 3: Creating or staring a Application
(myvenv) C:\Djangoapps\myproj7>py manage.py startapp StudentApp

#---------------------------------------------------------------------------------------------
#Step 4: Goto settings.py and add "StudentApp" to the installed apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "StudentApp"
]
#---------------------------------------------------------------------------------------------
#step 5: Create urls.py in Application folder(StudentApp) and include in project urls

StudentApp---->rightclick---->newfile---->urls.py and write the following code

from django.urls import re_path
from StudentApp import views #or from . import views
urlpatterns=['
          re_path(r'^$',views.input),
          re_path(r'^comp$',views.compute)
          ]

#----------------------------------------------------------------------------------------------
#step 6: open urls.py in the project folder
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r'^StudentApp/',include('StudentApp.urls'))
]
#----------------------------------------------------------------------------------------------
#Step 7: Views.py and define input function

from django.shortcuts import render

# Create your views here.
def input(request):
    return render(request,'base.html')

#---------------------------------------------------------------------------------------------
#Step 8: Creating "templates" folder and within it create "base.html"

myproj7(outer folder)---->right click----->newfolder---->"templates"

"templates"---->right click----->newfile---->base.html

#base.html

<html>
<body bgcolor="yellow" text="red">
  <form action="./comp" method="get">
    <h1><U>STUDENT DETAILS </U></h1>
    <h2>ENTER STUDENT NAME:<input type="text" name="t1" size="15"></h2>
    <h2>ENTER STUDENT ROLLNO:<input type="text" name="t2" size="15"></h2>
    <h2>ENTER STUDENT BRANCH:<input type="text" name="t3" size="15"></h2>
    <h2>ENTER STUDENT COLLEGE:<input type="text" name="t4" size="15"></h2>
    <h2>ENTER MARKS OF MATHS:<input type="text" name="t5" size="5"></h2>
    <h2>ENTER MARKS OF PHYSICS:<input type="text" name="t6" size="5"></h2>
    <h2>ENTER MARKS OF CHEMISTRY:<input type="text" name="t7" size="5"></h2>
    <input type="submit" value="SUBMIT">
    <input type="reset" value="CLEAR">
  </form>
  </body>
  </html>

#---------------------------------------------------------------------------------------------
#Step 9: Goto views.py and define compute function
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def input(request):
    return render(request,'base.html')

def compute(request):
    stdname=request.GET['t1']
    rollno=int(request.GET['t2'])
    branch=request.GET['t3']
    college=request.GET['t4']
    maths=int(request.GET['t5'])
    physics=int(request.GET['t6'])
    chemistry=int(request.GET['t7'])
    total=maths+physics+chemistry
    avg=total/3
    return HttpResponse("<html><body bgcolor='yellow' text='red'><h2>STUDENT NAME:"+stdname+
                        "<br>STUDENT ROLLNO:"+str(rollno)+
                        "<br>STUDENT BRANCH:"+branch+
                        "<br>STUDENT COLLEGE:"+college+
                        "<br>MATHS:"+str(maths)+
                        "<br>PHYSICS:"+str(physics)+
                        "<br>CHEMISTRY:"+str(chemistry)+
                        "<br>TOTAL MARKS:"+str(total)+
                        "<br>AVERAGE:"+str(avg)+"</h2></body></html>")


#----------------------------------------------------------------------------------------------
#Step 10: Adding templates folder path to settings.py

import os
TEMPLATE_DIR=os.path.join(BASE_DIR,'templates')  #add this after BASE_DIR

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATE_DIR],

#---------------------------------------------------------------------------------------------
#step 11: migrate

(myvenv) C:\Djangoapps\myproj7>py manage.py migrate

#--------------------------------------------------------------------------------------------
#step 12: runserver

(myvenv) C:\Djangoapps\myproj7>py manage.py runserver

#------------------------------------------------------------------------------------------
#step 13: Giving request

http://127.0.0.1:8000/StudentApp/

STUDENT DETAILS
ENTER STUDENT NAME:
Ajay
ENTER STUDENT ROLLNO:
501
ENTER STUDENT BRANCH:
CSE
ENTER STUDENT COLLEGE:
JNTU
ENTER MARKS OF MATHS:
90
ENTER MARKS OF PHYSICS:
50
ENTER MARKS OF CHEMISTRY:
80




#Note: for get request, we can see all the details entered within the browser window
http://127.0.0.1:8000/StudentApp/comp?t1=Ajay&t2=501&t3=CSE&t4=JNTU&t5=90&t6=50&t7=80










































































