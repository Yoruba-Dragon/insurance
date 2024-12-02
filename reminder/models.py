from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError

class Policy(models.Model): #Policy model
    POLICY_TYPE_CHOICES = [
        ('health', 'Health'),
        ('vehicle', 'Vehicle'),
        ('life', 'Life'),
        ('home', 'Home'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="policies")
    policy_number = models.CharField(max_length=20, unique=True, validators=[RegexValidator(r'^[A-Z0-9]{10,20}$', "Invalid policy number format.")])
    provider_name = models.CharField(max_length=100)
    policy_type = models.CharField(max_length=255, choices=POLICY_TYPE_CHOICES)
    start_date = models.DateField()
    expiry_date = models.DateField()
    reminder_date = models.DateField()


    def clean(self):# Policy validation in order to store only valid policies
        if self.expiry_date <= timezone.now().date():
            raise ValidationError("Expiry date must be in the future.")
        if self.reminder_date >= self.expiry_date:
            raise ValidationError("Reminder date must be before the expiry date.")
 
    def __str__(self):
        return f"{self.policy_number} - {self.policy_type}"
