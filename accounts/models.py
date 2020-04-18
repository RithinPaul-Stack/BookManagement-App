from django.db import models
from django.dispatch import receiver
# Create your models here.
from django.db.models.signals import pre_save
from django.contrib.auth.models import User

@receiver(pre_save, sender=User)
def update_username_from_email(sender, instance, **kwargs):
    instance.email = instance.email