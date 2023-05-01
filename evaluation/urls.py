from django.urls import path
from .views import (factor_list,start_evaluation,evaluation_form,course_evaluation,course_evaluation_form,course_evaluation_save,
                    colleague_evaluation,colleague_evaluation_form,colleague_evaluation_save)
               
app_name ='evaluation'
urlpatterns = [
    path('institution/factors',factor_list,name='factor-list'),
    path('institution/start-evaluation',start_evaluation,name='start-evaluation'),
    path('institution/<int:c_id>/evaluation-form',course_evaluation_form,name='course-evaluation-form'),
    path('institution/course-evaluation/',course_evaluation,name='course-evaluation'),
    path('institution/course-evaluation-save/<int:c_id>/<int:e_id>',course_evaluation_save,name='course-evaluation-save'),

    path('institution/colleague-evaluation/',colleague_evaluation,name='colleague-evaluation'),
    path('institution/<int:t_id>/colleague-evaluation-form',colleague_evaluation_form,name='colleague-evaluation-form'),
    path('institution/colleague-evaluation-save/<int:t_id>/<int:e_id>',colleague_evaluation_save,name='colleague-evaluation-save'),
]
