from django.urls import path
from .views import factor_list
               
app_name ='evaluation'
urlpatterns = [
    path('factors',factor_list,name='factor-list'),
]
