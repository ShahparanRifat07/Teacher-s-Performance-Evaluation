# Generated by Django 4.1.6 on 2023-04-08 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholder', '0018_alter_course_course_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_students',
            field=models.ManyToManyField(related_name='course_students', to='stakeholder.student'),
        ),
    ]
