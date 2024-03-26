from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate

def home(request):
    return render(request,'index.html')
def about(request):
    return render(request, 'about.html')
def query(request):
    return render(request, 'query.html')
def profile(request):
    return render(request, 'profile.html')
def register(request):
    return render(request, 'register.html')
def login(request):
    return render(request, 'login.html')