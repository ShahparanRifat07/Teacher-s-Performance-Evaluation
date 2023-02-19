from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from stakeholder.models import Institution, Student, Parent
from django.contrib.auth.models import User
from nameparser import HumanName


@receiver(pre_save, sender=Institution)
def create_admin_for_institution(sender, instance, *args, **kwargs):
    if instance.id is None:
        username = instance._username
        full_name = instance._full_name
        email = instance._email
        password = instance._password

        name = HumanName(full_name)
        first_name = name.first
        last_name = name.last

        user = User(username=username, first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        user.save()

        instance.institution_admin = user


@receiver(pre_save, sender=Student)
def create_user_for_student(sender, instance, *args, **kwargs):
    if instance.id is None:
        first_name = instance.first_name
        last_name = instance.last_name
        email = instance.email
        username = instance._student_username
        password = instance._student_password

        user = User(username=username, first_name=first_name, last_name=last_name, email = email)
        user.set_password(password)
        user.save()

        instance.user = user

@receiver(post_save, sender=Student)
def create_post_save_parent_for_student(sender, instance, created, *args, **kwargs):
    if created:
        parents_username = instance._parent_username
        phone_number = instance._parent_phone_number
        password = instance._parent_password

        user = User(username=parents_username)
        user.set_password(password)
        user.save()

        parent = Parent(user=user, phone_number=phone_number,institution = instance.institution,student = instance)
        parent.save()
