from django.contrib import admin
from .models import InstitutionTag,Factor,StakeholderTag, Question,EvaluationEvent
# Register your models here.

admin.site.register(InstitutionTag)
admin.site.register(Factor)
admin.site.register(StakeholderTag)
admin.site.register(Question)
admin.site.register(EvaluationEvent)