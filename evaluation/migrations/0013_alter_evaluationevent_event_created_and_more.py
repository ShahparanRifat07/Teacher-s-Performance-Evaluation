# Generated by Django 4.1.6 on 2023-04-17 01:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0012_rename_complete_evaluationevent_is_complete_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluationevent',
            name='event_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 17, 1, 0, 29, 635057, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='evaluationevent',
            name='is_complete',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='evaluationevent',
            name='is_published',
            field=models.BooleanField(),
        ),
    ]