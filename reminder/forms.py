from django import forms
from .models import Policy

class PolicyForm(forms.ModelForm): # Policy form for adding new policies
    class Meta:
        model = Policy
        fields = ['policy_number', 'policy_type', 'provider_name', 'start_date', 'expiry_date', 'reminder_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'expiry_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'reminder_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'policy_number': forms.TextInput(attrs={'class': 'form-control'}),
            'policy_type': forms.Select(attrs={'class': 'form-control'}),
            'provider_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
