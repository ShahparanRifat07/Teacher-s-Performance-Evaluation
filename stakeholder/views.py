from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import Institution,Student,Parent,Department
from django.http import HttpResponse

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



def add_student(request):
    if request.user.is_authenticated:
        institution = Institution.objects.filter(institution_admin=request.user)
        if institution is not None:
            institution_admin = institution[0].institution_admin
            if request.method == 'POST':
                first_name = request.POST.get('first_name')
                last_name = request.POST.get('last_name')
                student_id = request.POST.get('student_id')
                father_name = request.POST.get('father_name')
                mother_name = request.POST.get('mother_name')
                gender = request.POST.get('gender')
                dob = request.POST.get('dob')
                phone = request.POST.get('phone')
                department = request.POST.get('department')
                student_username = request.POST.get('student_username')
                email = request.POST.get('email')
                student_password = request.POST.get('student_password')
                parent_username = request.POST.get('parent_username')
                parent_phone = request.POST.get('parent_phone')
                parent_password = request.POST.get('parent_password')
                address = request.POST.get('address')
                city = request.POST.get('city')
                state = request.POST.get('state')
                zipcode = request.POST.get('zipcode')


                dept = Department.objects.get(id=department)
                student = Student(first_name = first_name,last_name = last_name,student_id = student_id,father_name=father_name,
                                    mother_name = mother_name, gender = gender,dob=dob,phone_number = phone,email = email,
                                    address = address,city=city,state=state,zipcode=zipcode,institution= institution[0],department = dept)
                

                student._student_username = student_username
                student._student_password = student_password
                student._parent_username = parent_username
                student._parent_phone_number = parent_phone
                student._parent_password = parent_password

                student.save()

                return redirect('add-student')
            if request.method == 'GET':
                departments = Department.objects.filter(institution = institution[0])
                context = {
                    'departments' : departments,
                }
                return render(request,'add_student.html',context)
        else:
            return HttpResponse("You are not allowed")
    else:
        return redirect('login')
