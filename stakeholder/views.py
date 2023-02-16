from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import Institution

# Create your views here.


def register(request):
    if request.method == "POST":
        institution_name = request.POST.get("institution_name")
        institution_code = request.POST.get("institution_code")
        established_year = request.POST.get("established_year")
        institution_type = request.POST.get("institution_type")
        institution_head = request.POST.get("institution_head")
        location = request.POST.get("location")
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        institution = Institution(institution_name=institution_name, institution_code=institution_code,
                                  established_year=established_year, institution_type=institution_type, institution_head=institution_head,
                                  location=location)

        institution._full_name = fullname
        institution._email = email
        institution._username = username
        institution._password = password

        institution.save()

        return redirect("login")
    elif request.method == "GET":
        return render(request, "register.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        
        try:
            user = authenticate(username= username,password = password)
            if user is not None:
                institution = Institution.objects.filter(institution_admin=user)
                if institution is not None:
                    print(institution[0].institution_admin)
                    return redirect("login")
                else:
                    print("not admin")
                    return redirect("login")
            else:
                print("no user found")
                return redirect("login")
        except:
            print("user does not exits")
            return redirect("login")
    elif request.method == "GET":
        return render(request, 'login.html')
