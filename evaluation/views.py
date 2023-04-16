from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from stakeholder.models import Institution,Student,Parent,Department,Teacher,Course,Administrator
from .models import Factor,StakeholderTag,Question,InstitutionTag,EvaluationEvent
from django.core.exceptions import PermissionDenied
from django.db import transaction
from django.db.models import Q
from django.utils import timezone
from datetime import datetime, time, timedelta
from django.http import HttpResponse, FileResponse, HttpResponseNotFound
# Create your views here.


def factor_list(request):
    if request.user.is_authenticated:
        institution = Institution.objects.filter(institution_admin=request.user)
        if institution:
            factors = Factor.objects.filter(institution=institution[0])
            context={
                "factors" : factors,
                'admin' : institution[0].institution_admin,
            }
            return render(request,'factor_list.html',context)
        else:
            raise PermissionDenied("You are not allowed")
    else:
        return redirect('stakeholder:login')


def start_evaluation(request):
    if request.user.is_authenticated:
        institution = Institution.objects.filter(institution_admin=request.user).first()
        if institution:
            factors = Factor.objects.filter(institution=institution)
            #creating factors for institutions
            stakeholder_tag = StakeholderTag.objects.all()
            institution_tag = InstitutionTag.objects.all()

            #stakeholders
            student = stakeholder_tag[0]
            teacher = stakeholder_tag[1]
            self = stakeholder_tag[2]
            parent = stakeholder_tag[3]
            administrator = stakeholder_tag[4]

            #institutions
            primary = institution_tag[0]
            secondary = institution_tag[1]
            tertiary = institution_tag[2]


            if request.method == "POST":
                stakeholders = request.POST.getlist('stakeholder')
                factors = request.POST.getlist('factors')
                start_date = request.POST.get('start_date')
                end_date = request.POST.get('end_date')

                evaluation_event = EvaluationEvent(institution = institution,start_date = start_date, end_date = end_date)
                evaluation_event.save()
                with transaction.atomic():
                    for id in stakeholders:
                        stakeholder = StakeholderTag.objects.get(id=id)
                        evaluation_event.stakeholder_tag.add(stakeholder)

                    for id in factors:
                        factor = Factor.objects.get(id=id)
                        evaluation_event.factor.add(factor)
                return redirect("evaluation:start-evaluation")

            if request.method == "GET":
                context={
                    "factors" : factors,
                    "student" : student,
                    "teacher" : teacher,
                    "self" : self,
                    "administrator" : administrator,
                    "parent" : parent,

                    "primary" : primary,
                    "secondary" : secondary,
                    "tertiary" : tertiary,
                    
                    'admin' : institution.institution_admin,
                }
            
                return render(request, 'create_evaluation.html',context)
        else:
            raise PermissionDenied("You are not allowed")
    else:
        return redirect('stakeholder:login')
    

def evaluation_form(request):
    if request.user.is_authenticated:
        stakeholder_tag = StakeholderTag.objects.all()
        #stakeholders
        student_tag = stakeholder_tag[0]
        teacher_tag = stakeholder_tag[1]
        self_tag = stakeholder_tag[2]
        parent_tag = stakeholder_tag[3]
        administrator_tag = stakeholder_tag[4]

        now = timezone.now()

        student = Student.objects.filter(user = request.user).first()
        if student:
            evaluaton_event = EvaluationEvent.objects.filter(start_date__gte=now).order_by('start_date').first()

            start_time = timezone.make_aware(datetime.combine(evaluaton_event.start_date, time.min))
            end_time = timezone.make_aware(datetime.combine(evaluaton_event.end_date, time.max))

            if start_time <= now <= end_time:
                factors = evaluaton_event.factor.all()
                questions = {}
                for factor in factors:
                    question = Question.objects.filter(Q(factor = factor) & Q(stakeholder_tag = student_tag))
                    questions[factor] = question
                

                for factor, questions in questions.items():
                    for question in questions:
                        print('\t', question)
                context = {
                    "questions" : questions
                }
                return render(request, 'evaluation_form.html',context)
            
        else:
            return HttpResponse('This view is not available at this time.')
    else:
        return redirect('stakeholder:login')