from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import *
from .forms import UserAdminCreationForm, UserDonateForm
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class UserList(LoginRequiredMixin,ListView):
    model = User
    template_name = 'donation/user_list.html'
    context_object_name = 'user_list'

class UserCreate(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'donation/user_create.html'
    form_class = UserAdminCreationForm
    
    context_object_name = 'user_create'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    success_url = '/manage'

class UserDelete(LoginRequiredMixin,DeleteView):
    model = User
    template_name = 'donation/user_delete.html'
    
    success_url = '/manage'

class UserUpdate(LoginRequiredMixin,UpdateView):
    model = User
    template_name = 'donation/user_update.html'
    fields = ['first_name', 'last_name', 'email', 'role_opt']
    success_url = '/manage'




class DonationList(LoginRequiredMixin, ListView):
    model = Donation
    template_name = 'donation/donation_list.html'
    context_object_name = 'donation_list'

class DonationCreateType(LoginRequiredMixin, CreateView):
    model = Donation
    template_name = 'donation/donationtype_create.html'
    fields = ['donation_type', 'slug']

    success_url = '/donations'


# contribute page
class UserView(LoginRequiredMixin, ListView):
    model = Donation
    template_name = 'donation/user_view.html'
    context_object_name = 'donation_type'
# user donation form
class UserDonate(LoginRequiredMixin,CreateView):
    model = Donation
    template_name ='donation/donation_create.html'
    form_class = UserDonateForm




class Cart(LoginRequiredMixin, ListView):
    model = Cart

    template_name = 'donation/cart.html'
    context_object_name = 'cart'