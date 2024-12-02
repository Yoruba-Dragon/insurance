from django.contrib import admin
from .models import Policy
from django_celery_beat.models import PeriodicTask, IntervalSchedule

@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ('policy_number', 'policy_type', 'provider_name', 'expiry_date', 'reminder_date', 'user')
    search_fields = ('policy_number', 'provider_name', 'user__username')
    list_filter = ('policy_type', 'expiry_date')
    ordering = ('-expiry_date',)

# Optionally, register PeriodicTask and IntervalSchedule if not already
# admin.site.register(PeriodicTask)
# admin.site.register(IntervalSchedule)
