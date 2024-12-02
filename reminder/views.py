# reminders/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Policy
from .forms import PolicyForm
from django.contrib import messages

@login_required
def policy_list(request):
    policies = Policy.objects.filter(user=request.user).order_by('expiry_date')
    return render(request, 'reminders/policy_list.html', {'policies': policies})

@login_required
def add_policy(request):
    if request.method == 'POST':
        form = PolicyForm(request.POST)
        if form.is_valid():
            policy = form.save(commit=False)
            policy.user = request.user
            policy.save()
            messages.success(request, 'Policy added successfully!')
            return redirect('policy_list')
    else:
        form = PolicyForm()
    return render(request, 'reminders/add_policy.html', {'form': form})

@login_required
def edit_policy(request, pk):
    policy = get_object_or_404(Policy, pk=pk, user=request.user)
    if request.method == 'POST':
        form = PolicyForm(request.POST, instance=policy)
        if form.is_valid():
            form.save()
            messages.success(request, 'Policy updated successfully!')
            return redirect('policy_list')
    else:
        form = PolicyForm(instance=policy)
    return render(request, 'reminders/edit_policy.html', {'form': form})

@login_required
def delete_policy(request, pk):
    policy = get_object_or_404(Policy, pk=pk, user=request.user)
    if request.method == 'POST':
        policy.delete()
        messages.success(request, 'Policy deleted successfully!')
        return redirect('policy_list')
    return render(request, 'reminders/delete_policy.html', {'policy': policy})

class PolicyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Policy
    form_class = PolicyForm
    template_name = 'reminders/edit_policy.html'
    success_url = reverse_lazy('policy_list')

    def test_func(self):
        policy = self.get_object()
        return self.request.user == policy.user

class PolicyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Policy
    template_name = 'reminders/delete_policy.html'
    success_url = reverse_lazy('policy_list')

    def test_func(self):
        policy = self.get_object()
        return self.request.user == policy.user
