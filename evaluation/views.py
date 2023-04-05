from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from stakeholder.models import Institution,Student,Parent,Department,Teacher,Course,AdministrativeRole,Administrator
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