from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from stakeholder.models import Institution
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