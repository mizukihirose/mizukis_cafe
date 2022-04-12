from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from .models import Beans

# Create your views here.
def index(request):
  all_beans = Beans.objects.all()
  return render(request, 'mizukis_cafe/index.html', {'beans':all_beans})


def add_beans(request):
  return render(request, 'mizukis_cafe/add_beans.html')


def modify_db(request):
  return redirect(reverse('mizukis_cafe:index'))