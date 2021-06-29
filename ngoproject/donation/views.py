from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import DonationType, User, Donation
from .forms import UserAdminCreationForm
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class UserList(ListView):
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

class UserDelete(DeleteView):
    model = User
    template_name = 'donation/user_delete.html'
    
    success_url = '/manage'

class UserUpdate(UpdateView):
    model = User
    template_name = 'donation/user_update.html'
    fields = ['first_name', 'last_name', 'email', 'role_opt']
    success_url = '/manage'




class DonationList(ListView):
    model = Donation
    template_name = 'donation/donation_list.html'
    context_object_name = 'donation_list'

class UserDonate(CreateView):
    model = Donation
    template_name ='donation/donation_create.html'
    fields = '__all__'


class DonationCreate(CreateView):
    model = Donation
    template_name = 'donation/donationtype_create.html'
    fields = ['donation_type']

    success_url = '/donations'

class UserView(ListView):
    model = Donation
    template_name = 'donation/user_view.html'
    context_object_name = 'donation_type'

class GiveDonation(CreateView):
    model = Donation
    template_name = 'donation/give_donation.html'
    fields = '__all__'

   # success_url = '/cart'

class Cart(ListView):
    model = Donation
    template_name = 'donation/cart.html'
    context_object_name = 'items'