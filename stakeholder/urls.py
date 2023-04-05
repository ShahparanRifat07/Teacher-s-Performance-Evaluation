from django.urls import path
from .views import (register,user_login,add_student,dashboard,user_logout,view_student_list,add_teacher,
                    add_department,view_department_list,view_teacher_list,add_student_excel,
                    admin_dashboard,student_dashboard,parent_dashboard,teacher_dashboard,administrator_dashboard,
                    download_student_excel,add_course,
                    add_administrative_role,add_administrator)

app_name ='stakeholder'
urlpatterns = [
    path('register/',register,name="register"),
    path('login/',user_login,name="login"), 
    path('logout/',user_logout,name="logout"),
    path('',dashboard,name="dashboard"),
    path('institution/admin-dashboard/',admin_dashboard,name="admin-dashboard"),
    path('institution/student-dashboard/',student_dashboard,name="student-dashboard"),
    path('institution/parent-dashboard/',parent_dashboard,name="parent-dashboard"),
    path('institution/teacher-dashboard/',teacher_dashboard,name="teacher-dashboard"),
    path('institution/administrator-dashboard/',administrator_dashboard,name="administrator-dashboard"),
    path('institution/add-student/',add_student,name="add-student"),
    path('institution/add-student-excel/',add_student_excel,name="add-student-excel"),
    path('institution/download-student-excel-file/',download_student_excel,name="download-student-excel"),
    path('institution/student-list/',view_student_list,name="student-list"),
    path('institution/add-teacher/',add_teacher,name="add-teacher"),
    path('institution/teacher-list/',view_teacher_list,name="teacher-list"),
    path('institution/add-department/',add_department,name="add-department"),
    path('institution/department-list/',view_department_list,name="department-list"),
    path('institution/add-course/',add_course,name="add-course"),

    path('institution/add-administrative-role/',add_administrative_role,name="add-administrative-role"),
    path('institution/add-administrator/',add_administrator,name="add-administrator"),
]
