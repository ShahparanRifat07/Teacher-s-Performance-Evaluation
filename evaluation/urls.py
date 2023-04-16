from django.urls import path
from .views import factor_list,start_evaluation,evaluation_form
               
app_name ='evaluation'
urlpatterns = [
    path('institution/factors',factor_list,name='factor-list'),
    path('institution/start-evaluation',start_evaluation,name='start-evaluation'),
    path('institution/evaluation-form',evaluation_form,name='evaluation-form'),
]
