from django.db import models

# Create your models here.
class Notifications(models.Model):# Notification model
    NOTIFICATION_TYPES = [
        ("USER_NOTIFICATION", "User Notification"),
        ("ACCOUNT_NOTIFICATION", "Account Notification"),
        ("SECURITY_NOTIFICATION", "Security Notification"),
    ]

    STATUS_CHOICES = [
        ("READ", "Read"),
        ("UNREAD", "Unread"),
    ]

    
    notification_type = models.CharField(max_length=30, choices=NOTIFICATION_TYPES)
    content = models.TextField()
    status = models.CharField(max_length=10, default='UNREAD', choices=STATUS_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Notification ID: {self.pk} - Type: {self.get_notification_type_display()} - User: {self.user.username}"
