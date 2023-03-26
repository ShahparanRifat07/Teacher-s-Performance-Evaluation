from django.contrib import admin
from .models import InstitutionTag,Factor,StakeholderTag, Question
# Register your models here.

admin.site.register(InstitutionTag)
admin.site.register(Factor)
admin.site.register(StakeholderTag)
admin.site.register(Question)