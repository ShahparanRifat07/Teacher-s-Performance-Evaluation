from django.urls import path
from .views import factor_list,start_evaluation
               
app_name ='evaluation'
urlpatterns = [
    path('institution/factors',factor_list,name='factor-list'),
    path('institution/start-evaluation',start_evaluation,name='start-evaluation'),
]
