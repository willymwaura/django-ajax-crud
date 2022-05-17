from django.contrib.messages.api import info
from django.http import request,JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import Feature
from django.contrib.auth.models import User, UserManager,auth
from django .contrib import messages
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
     return render(request,"index.html")
def listnames(request):
     feature=Feature.objects.all()
     return JsonResponse({"feature":list(feature.values())})

