# Generated by Django 4.1.6 on 2023-04-17 00:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0011_evaluationevent_complete_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evaluationevent',
            old_name='complete',
            new_name='is_complete',
        ),
        migrations.RenameField(
            model_name='evaluationevent',
            old_name='publish',
            new_name='is_published',
        ),
        migrations.AlterField(
            model_name='evaluationevent',
            name='event_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 17, 0, 50, 37, 986637, tzinfo=datetime.timezone.utc)),
        ),
    ]
