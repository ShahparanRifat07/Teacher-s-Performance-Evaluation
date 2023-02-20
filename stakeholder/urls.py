from django.urls import path
from .views import register,user_login,add_student,dashboard,user_logout,view_student_list,add_teacher,add_department,view_department_list

urlpatterns = [
    path('register/',register,name="register"),
    path('login/',user_login,name="login"),
    path('add_student/',add_student,name="add-student"),
    path('dashboard/',dashboard,name="dashboard"),
    path('logout/',user_logout,name="logout"),
    path('student_list/',view_student_list,name="student-list"),
    path('add_teacher/',add_teacher,name="add-teacher"),
    path('add_department/',add_department,name="add-department"),
    path('department_list/',view_department_list,name="department-list"),
]
