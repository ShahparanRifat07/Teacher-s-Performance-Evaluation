# Generated by Django 4.1.6 on 2023-05-01 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('dept_head', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=128)),
                ('institution_code', models.CharField(max_length=11)),
                ('established_year', models.CharField(max_length=4)),
                ('institution_type', models.CharField(choices=[('1', 'Primary'), ('2', 'Secondary'), ('3', 'Tertiary'), ('4', 'Other')], max_length=1)),
                ('institution_head', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=128)),
                ('apply_date', models.DateField(default=django.utils.timezone.now)),
                ('approved', models.BooleanField(default=False)),
                ('institution_admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('teacher_id', models.CharField(max_length=32)),
                ('designation', models.CharField(max_length=64)),
                ('joining_date', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('1', 'Male'), ('2', 'Female'), ('3', 'Others')], max_length=2)),
                ('dob', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(max_length=16)),
                ('image', models.ImageField(default='default.jpg', upload_to='Profile_Picture')),
                ('email', models.CharField(max_length=64)),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=64, null=True)),
                ('state', models.CharField(blank=True, max_length=64, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=64, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stakeholder.department')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stakeholder.institution')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('student_id', models.CharField(max_length=11)),
                ('father_name', models.CharField(max_length=64)),
                ('mother_name', models.CharField(max_length=64)),
                ('gender', models.CharField(choices=[('1', 'Male'), ('2', 'Female'), ('3', 'Others')], max_length=2)),
                ('dob', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(max_length=16)),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=64, null=True)),
                ('state', models.CharField(blank=True, max_length=64, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=64, null=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='Profile_Picture')),
                ('email', models.CharField(max_length=64)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stakeholder.department')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stakeholder.institution')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=11)),
                ('image', models.ImageField(default='default.jpg', upload_to='Profile_Picture')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stakeholder.institution')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stakeholder.student')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stakeholder.institution'),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=16)),
                ('course_name', models.CharField(max_length=128)),
                ('section', models.CharField(max_length=2)),
                ('course_students', models.ManyToManyField(related_name='course_students', to='stakeholder.student')),
                ('course_teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stakeholder.teacher')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stakeholder.institution')),
            ],
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=64, null=True)),
                ('last_name', models.CharField(blank=True, max_length=64, null=True)),
                ('administrative_id', models.CharField(blank=True, max_length=64, null=True)),
                ('role', models.CharField(blank=True, max_length=128, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='Profile_Picture')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stakeholder.institution')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
