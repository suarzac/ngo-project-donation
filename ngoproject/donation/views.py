from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

from .models import User, Donation
from django.views.generic import CreateView, DetailView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class UserList(ListView):
    model = User
    template_name = 'donation/user_list.html'
    context_object_name = 'user_list'

class UserCreate(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'donation/user_create.html'
    fields = ['first_name', 'last_name', 'usr_email', 'usr_password', 'role_opt']
    
    context_object_name = 'user_create'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    success_url = '/'

class UserDelete(DeleteView):
    model = User
    template_name = 'donation/user_delete.html'
    
    success_url = '/'