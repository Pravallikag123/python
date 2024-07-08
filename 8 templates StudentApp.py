
#Develop a Django Project to accept Student details and print them
        
Application Name:StudentApp

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "StudentApp"
]

from django.urls import re_path
from StudentApp import views #or from . import views
urlpatterns=['
          re_path(r'^$',views.input),
          re_path(r'^comp$',views.compute)
          ]


from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r'^StudentApp/',include('StudentApp.urls'))
]


from django.shortcuts import render

# Create your views here.
def input(request):
    return render(request,'base.html')



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



import os
TEMPLATE_DIR=os.path.join(BASE_DIR,'templates')  #add this after BASE_DIR

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATE_DIR],

STUDENT DETAILS
ENTER STUDENT NAME:
s
ENTER STUDENT ROLLNO:
50
ENTER STUDENT BRANCH:
CSE
ENTER STUDENT COLLEGE:
por
ENTER MARKS OF MATHS:
90
ENTER MARKS OF PHYSICS:
50
ENTER MARKS OF CHEMISTRY:
80













































































