# Generated by Django 4.1.6 on 2023-04-17 01:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0014_alter_evaluationevent_event_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluationevent',
            name='factor',
        ),
        migrations.AddField(
            model_name='evaluationevent',
            name='administrator_factor',
            field=models.ManyToManyField(related_name='evaluation_administrator_factor', to='evaluation.factor'),
        ),
        migrations.AddField(
            model_name='evaluationevent',
            name='parent_factor',
            field=models.ManyToManyField(related_name='evaluation_parent_factor', to='evaluation.factor'),
        ),
        migrations.AddField(
            model_name='evaluationevent',
            name='self_factor',
            field=models.ManyToManyField(related_name='evaluation_self_factor', to='evaluation.factor'),
        ),
        migrations.AddField(
            model_name='evaluationevent',
            name='student_factor',
            field=models.ManyToManyField(related_name='evaluation_student_factor', to='evaluation.factor'),
        ),
        migrations.AddField(
            model_name='evaluationevent',
            name='teacher_factor',
            field=models.ManyToManyField(related_name='evaluation_teacher_factor', to='evaluation.factor'),
        ),
        migrations.AlterField(
            model_name='evaluationevent',
            name='event_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 17, 1, 23, 20, 270516, tzinfo=datetime.timezone.utc)),
        ),
    ]
