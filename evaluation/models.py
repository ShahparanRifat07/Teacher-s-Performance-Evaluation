from django.db import models
from stakeholder.models import Institution,Department,Teacher,Student,Parent

# Create your models here.


class StakeholderTag(models.Model):
    name=models.CharField(max_length=64)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name

class InstitutionTag(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name

class Factor(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True,null=True)
    institution_tag = models.ManyToManyField(InstitutionTag)
    stakeholder_tag = models.ManyToManyField(StakeholderTag)
    institution = models.ForeignKey(Institution,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Question(models.Model):
    question = models.TextField()
    stakeholder_tag = models.ManyToManyField(StakeholderTag)
    factor = models.ForeignKey(Factor, on_delete=models.CASCADE)
    # institution = models.ForeignKey(Institution,on_delete=models.CASCADE)

    def __str__(self):
        return self.question