from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from stakeholder.models import Institution,Student,Parent,Department,Teacher,Course,Administrator
from .models import Factor,StakeholderTag,Question,InstitutionTag
from django.core.exceptions import PermissionDenied
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
    