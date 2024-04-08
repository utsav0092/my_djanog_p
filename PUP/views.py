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

def register(request):
    if request.method == 'POST':
        # user_name = request.POST['user_name']
        # user_password = request.POST['user_password']
        # data = User.objects.create_user(user_name=user_name, user_password=user_password)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form':form})

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request = request, data= request.POST)
        if form.is_valid():
            uname = form.cleaned_data['Username']
            upass = form.cleaned_data['Password']
            user = authenticate(Username = uname, Password = upass)
            return render(request, 'profile.html')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})