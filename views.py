from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def my_index_page(request):
  return HttpResponse("hello welcome to my index page")