from django.apps import AppConfig

class RemindersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reminder'

    # def ready(self):
    #     import reminders.signals  # noqa