# Generated by Django 4.1.6 on 2023-04-06 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholder', '0014_administrator_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrator',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='Profile_Picture'),
        ),
        migrations.AddField(
            model_name='parent',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='Profile_Picture'),
        ),
    ]
