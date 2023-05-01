from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from stakeholder.models import Institution,Student,Parent,Department,Teacher,Course,Administrator
from .models import Factor,StakeholderTag,Question,InstitutionTag,EvaluationEvent,StudentEvaluationResponse
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

                student_factors = request.POST.getlist('student_factors')
                teacher_factors = request.POST.getlist('teacher_factors')
                parent_factors = request.POST.getlist('parent_factors')
                self_factors = request.POST.getlist('self_factors')
                administrator_factors = request.POST.getlist('administrator_factors')
                
                start_date = request.POST.get('start_date')
                end_date = request.POST.get('end_date')

                evaluation_event = EvaluationEvent(institution = institution,start_date = start_date, end_date = end_date,is_start = True)
                evaluation_event.save()
                with transaction.atomic():
                    for id in stakeholders:
                        stakeholder = StakeholderTag.objects.get(id=id)
                        evaluation_event.stakeholder_tag.add(stakeholder)

                    for id in student_factors:
                        factor = Factor.objects.get(id=id)
                        evaluation_event.student_factor.add(factor)
                    
                    for id in teacher_factors:
                        factor = Factor.objects.get(id=id)
                        evaluation_event.teacher_factor.add(factor)
                    
                    for id in parent_factors:
                        factor = Factor.objects.get(id=id)
                        evaluation_event.parent_factor.add(factor)
                    
                    for id in self_factors:
                        factor = Factor.objects.get(id=id)
                        evaluation_event.self_factor.add(factor)
                    
                    for id in administrator_factors:
                        factor = Factor.objects.get(id=id)
                        evaluation_event.administrator_factor.add(factor)
                       
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
    

def course_evaluation(request):
    if request.user.is_authenticated:
        now = timezone.now()
        student = Student.objects.filter(user = request.user).first()
        if student:
            evaluaton_event = EvaluationEvent.objects.filter(Q(institution = student.institution) & Q(is_start = True) & Q(is_end = False)).first()
            if evaluaton_event:
                start_time = timezone.make_aware(datetime.combine(evaluaton_event.start_date, time.min))
                end_time = timezone.make_aware(datetime.combine(evaluaton_event.end_date, time.max))
                if start_time <= now <= end_time:
                    courses = student.course_students.all()
                    evaluation_started = True
                    context = {
                    'courses' : courses, 
                    'evaluation_started' : evaluation_started,
                    }
                    return render(request, 'course_evaluation.html',context)
                else:
                    evaluation_started = False
                    context = {
                        'evaluation_started' : evaluation_started,
                    }
                    return render(request, 'course_evaluation.html',context)
            else:
                evaluation_started = False
                context = {
                    'evaluation_started' : evaluation_started,
                }
                return render(request, 'course_evaluation.html',context)
        else:
            return HttpResponse("You are not allowed to view this")
    else:
        return redirect('stakeholder:login')






def course_evaluation_form(request,c_id):
    if request.user.is_authenticated:
        stakeholder_tag = StakeholderTag.objects.all()
        #stakeholders
        student_tag = stakeholder_tag[0]
        now = timezone.now()
        student = Student.objects.filter(user = request.user).first()
        if student:
            try:
                course = Course.objects.get(id = c_id)
            except:
                return HttpResponseNotFound("this course is not found")
            
            evaluaton_event = EvaluationEvent.objects.filter(Q(institution = student.institution) & Q(is_start = True) & Q(is_end = False)).first()
            if evaluaton_event:
                start_time = timezone.make_aware(datetime.combine(evaluaton_event.start_date, time.min))
                end_time = timezone.make_aware(datetime.combine(evaluaton_event.end_date, time.max))
                if start_time <= now <= end_time:
                    factors = evaluaton_event.student_factor.all()
                    questions = Question.objects.filter(Q(factor__in = factors) & Q(stakeholder_tag = student_tag))
                    evaluation_started = True
                    context = {
                        "evaluation_event": evaluaton_event,
                       "questions" : questions,
                       'evaluation_started' : evaluation_started,
                       "course":course,
                    }
                    return render(request, 'course_evaluation_form.html',context)
                else:
                    evaluation_started = False
                    context = {
                        'evaluation_started' : evaluation_started,
                    }
                    return render(request, 'course_evaluation_form.html',context)
            else:
                evaluation_started = False
                context = {
                    'evaluation_started' : evaluation_started,
                }
                return render(request, 'course_evaluation_form.html',context)
        else:
            return HttpResponse("You are not allowed to view this")
    else:
        return redirect('stakeholder:login')



def course_evaluation_save(request,c_id,e_id):
    if request.user.is_authenticated:
        student = Student.objects.filter(user = request.user).first()
        if student:
            try:
                course = Course.objects.get(id = c_id)   
            except:
                return HttpResponseNotFound("this course is not found")
            try:
                evaluation_event = EvaluationEvent.objects.get(id = e_id)
                if  evaluation_event.is_start == False:
                    return HttpResponse("evaluation event isn't started yet")
                if  evaluation_event.is_end == True:
                    return HttpResponse("evaluation event already finished")
            except:
                return HttpResponse("NO evaluation event found")
            
            if request.method == 'POST':
                # create an empty dictionary to store the question ids and answers
                answers = {}
        
                # loop through the POST data and extract the values for each question
                for key, value in request.POST.items():
                    if key.startswith('question-'):
                        # extract the question ID from the name attribute of the radio button
                        question_id = int(key.split('-')[1])
                        # store the answer value in the dictionary
                        answers[question_id] = value


                with transaction.atomic():
                    for question_id, rating in answers.items():
                        question = Question.objects.get(id = question_id)
                        student_question_response = StudentEvaluationResponse(evaluaton_event = evaluation_event,question = question,student = student,course = course,teacher = course.course_teacher,rating = str(rating))
                        student_question_response.save()
                return redirect("stakeholder:student-dashboard")
            else:
                return HttpResponse("not allowed")
            
        else:
            return HttpResponse("You are not allowed to view this")
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
            evaluaton_event = EvaluationEvent.objects.filter(Q(institution = student.institution) & Q(is_start = True) & Q(is_end = False)).first()
            if evaluaton_event:
                start_time = timezone.make_aware(datetime.combine(evaluaton_event.start_date, time.min))
                end_time = timezone.make_aware(datetime.combine(evaluaton_event.end_date, time.max))

                if start_time <= now <= end_time:
                    factors = evaluaton_event.student_factor.all()
                    questions = Question.objects.filter(Q(factor__in = factors) & Q(stakeholder_tag = student_tag))
                    context = {
                        "questions" : questions
                    }
                    return render(request, 'evaluation_form.html',context)
                else:
                    return HttpResponse("evaluation is not started yet")
            else:
                return HttpResponse("evaluation is not started yet")
        
        parent = Parent.objects.filter(user = request.user).first()
        if parent:
            evaluaton_event = EvaluationEvent.objects.filter(Q(institution = parent.institution) & Q(is_start = True) & Q(is_end = False)).first()

            if evaluaton_event:
                start_time = timezone.make_aware(datetime.combine(evaluaton_event.start_date, time.min))
                end_time = timezone.make_aware(datetime.combine(evaluaton_event.end_date, time.max))

                if start_time <= now <= end_time:
                    factors = evaluaton_event.parent_factor.all()

                    questions = Question.objects.filter(Q(factor__in = factors) & Q(stakeholder_tag = parent_tag))
                    context = {
                        "questions" : questions
                    }
                    return render(request, 'evaluation_form.html',context)
            else:
                return HttpResponse("evaluation is not started yet")
        
        teacher = Teacher.objects.filter(user = request.user).first()
        if teacher:
            evaluaton_event = EvaluationEvent.objects.filter(Q(institution = teacher.institution) & Q(is_start = True) & Q(is_end = False)).first()
            if evaluaton_event:
                start_time = timezone.make_aware(datetime.combine(evaluaton_event.start_date, time.min))
                end_time = timezone.make_aware(datetime.combine(evaluaton_event.end_date, time.max))

                if start_time <= now <= end_time:
                    factors = evaluaton_event.teacher_factor.all()
                    self_factors = evaluation_form.self_factor.all()
                    questions = Question.objects.filter(Q(factor__in = factors) & Q(stakeholder_tag = teacher_tag))
                    self_questions = Question.objects.filter(Q(factor__in = self_factors) & Q(stakeholder_tag = self_tag))
                    context = {
                        "questions" : questions,
                        "self_questions"  : self_questions,
                    }
                    
                    return render(request, 'evaluation_form.html',context)
            else:
                return HttpResponse('Evaluation is not started yet')
        
        administrator = Administrator.objects.filter(user = request.user).first()
        if administrator:
            evaluaton_event = EvaluationEvent.objects.filter(Q(institution = administrator.institution) & Q(is_start = True) & Q(is_end = False)).first()
            if evaluaton_event:
                start_time = timezone.make_aware(datetime.combine(evaluaton_event.start_date, time.min))
                end_time = timezone.make_aware(datetime.combine(evaluaton_event.end_date, time.max))

                if start_time <= now <= end_time:
                    factors = evaluaton_event.administrator_factor.all()
                    questions = Question.objects.filter(Q(factor__in = factors) & Q(stakeholder_tag = administrator_tag))
                    context = {
                        "questions" : questions
                    }
                    
                    return render(request, 'evaluation_form.html',context)
            else:
                return HttpResponse('Evaluation is not started yet')

    else:
        return redirect('stakeholder:login')