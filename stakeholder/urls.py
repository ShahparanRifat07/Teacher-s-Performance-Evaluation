from django.urls import path
from .views import register,user_login,add_student

urlpatterns = [
    path('register/',register,name="register"),
    path('login/',user_login,name="login"),
    path('add_student/',add_student,name="add-student"),
]
