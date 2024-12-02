from django.urls import path
from . import views

urlpatterns = [
    path('', views.policy_list, name='policy_list'),
    path('add/', views.add_policy, name='add_policy'),
    path('edit/<int:pk>/', views.PolicyUpdateView.as_view(), name='edit_policy'),
    path('delete/<int:pk>/', views.PolicyDeleteView.as_view(), name='delete_policy')
]
