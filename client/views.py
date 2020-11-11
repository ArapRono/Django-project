from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST["username"].strip().title()
        firstname = request.POST["first_name"].strip().title()
        lastname = request.POST["last_name"].strip().title()
        email = request.POST["email_phone_number"].strip()
        password_1 = request.POST["password_1"].strip().title()
        password_2 = request.POST["password_2"].strip().title()
        if password_1 == password_2:
            if User.objects.filter(username=username).exists():
                messages.warning(request, "The username is already taken")
                return redirect("signup")
            elif User.objects.filter(email = email).exists():
                messages.warning(request, "Email already exist")
                return redirect("signup")
            else:
                user = User.objects.create_user(username = username, email = email, password = password_1, first_name = firstname, last_name = lastname)
                user.save()
                return redirect("login") 
        else:
            messages.error(request, "The password does not match")
            return redirect("signup")
    else:
        return render(request,"signup.html")
def login(request):
    if request.method == "POST":
        username = request.POST["username"].strip().title()
        password = request.POST["password"].strip().title()
        user = authenticate(username = username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Invalid login credentials")
            return redirect("login")
        
    else:
        return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect("/")