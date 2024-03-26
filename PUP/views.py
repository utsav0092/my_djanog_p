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
def login(request):
    return render(request, 'login.html')
# def register(request):
#     return render(request, 'register.html')
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form':form})

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(Username = uname, Password = upass)
            return render(request, 'profile.html')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})