# Automatically set reminder_date based on expiry_date
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Policy
from django.utils import timezone
from datetime import timedelta

@receiver(pre_save, sender=Policy)
def set_reminder_date(sender, instance, **kwargs):
    if not instance.reminder_date:
        instance.reminder_date = instance.expiry_date - timedelta(days=30)  # 30 days before expiry
