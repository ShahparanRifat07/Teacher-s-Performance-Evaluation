# Generated by Django 4.1.6 on 2023-03-31 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholder', '0007_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stakeholder.teacher'),
        ),
    ]