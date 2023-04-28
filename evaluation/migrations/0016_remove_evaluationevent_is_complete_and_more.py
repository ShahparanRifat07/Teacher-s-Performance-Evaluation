# Generated by Django 4.1.6 on 2023-04-17 01:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0015_remove_evaluationevent_factor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluationevent',
            name='is_complete',
        ),
        migrations.RemoveField(
            model_name='evaluationevent',
            name='is_published',
        ),
        migrations.AlterField(
            model_name='evaluationevent',
            name='event_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 17, 1, 25, 54, 420665, tzinfo=datetime.timezone.utc)),
        ),
    ]