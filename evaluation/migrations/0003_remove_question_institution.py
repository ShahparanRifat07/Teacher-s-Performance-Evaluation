# Generated by Django 4.1.6 on 2023-03-26 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0002_alter_factor_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='institution',
        ),
    ]
