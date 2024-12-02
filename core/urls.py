from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('policies/', include('reminder.urls')),  # Reminders app
    path('users/', include('users.urls')),        # Users app
    path('', include('reminder.urls')),          # Redirect root to reminders
]
