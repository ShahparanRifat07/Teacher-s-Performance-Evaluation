from django.contrib import admin
from .models import InstitutionTag,Factor,StakeholderTag, Question,EvaluationEvent,StudentEvaluationResponse
# Register your models here.

admin.site.register(InstitutionTag)
admin.site.register(Factor)
admin.site.register(StakeholderTag)
admin.site.register(Question)
admin.site.register(EvaluationEvent)
admin.site.register(StudentEvaluationResponse)