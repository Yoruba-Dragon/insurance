from celery import shared_task
from django.core.mail import send_mail
from .models import Policy
from django.utils.timezone import now, timedelta

@shared_task
def send_policy_reminders():
    today = now().date()
    upcoming_policies = Policy.objects.filter(expiry_date=today + timedelta(days=7))
    for policy in upcoming_policies:
        if policy.email_notification:
            send_mail(
                "Insurance Renewal Reminder",
                f"Your policy {policy.policy_number} with {policy.provider} expires on {policy.expiry_date}.",
                "noreply@example.com",
                [policy.user.email],
            )
