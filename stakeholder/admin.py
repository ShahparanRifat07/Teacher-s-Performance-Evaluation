from django.contrib import admin
from .models import Institution,Student,Parent,Department,Teacher

# Register your models here.

admin.site.register(Institution)
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Department)
admin.site.register(Teacher)