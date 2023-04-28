# Generated by Django 4.1.6 on 2023-04-28 10:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0016_remove_evaluationevent_is_complete_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluationevent',
            name='is_end',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='evaluationevent',
            name='is_start',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='evaluationevent',
            name='event_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 28, 10, 32, 13, 817833, tzinfo=datetime.timezone.utc)),
        ),
    ]