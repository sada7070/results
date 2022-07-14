from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user=authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request,user)
            print("Logged in")
            return redirect('main/index')
            

    else:
        return render(request, "login.html")


def signup(request):
    if request.method == 'POST':
        firstName =request.POST['firstname']
        lastName =request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2= request.POST['password2']

        if password1 == password2:
            user=User.objects.create_user(username=username,email=email,password=password,first_name=firstName,last_name=lastName)
            print("user created")
            return redirect('/')

        else:
            print("Wrong password")

    else:
        return render(request,'signup.html')