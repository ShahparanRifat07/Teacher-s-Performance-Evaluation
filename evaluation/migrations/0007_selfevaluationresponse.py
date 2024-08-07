# Generated by Django 4.1.6 on 2023-05-02 22:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholder', '0001_initial'),
        ('evaluation', '0006_alter_evaluationevent_event_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelfEvaluationResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=1)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('evaluaton_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluation.evaluationevent')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluation.question')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stakeholder.teacher')),
            ],
        ),
    ]
