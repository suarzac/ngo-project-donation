from django.urls import path
from . import views

app_name = 'donation'

urlpatterns = [
    path('login', views.UserList.as_view(), name='login'), 
    path('manage', views.UserList.as_view(), name='user_list'),
    path('add', views.UserCreate.as_view(), name='user_create'),
    path('update/<slug:pk>', views.UserUpdate.as_view(), name='user_update'), 
    path('delete/<slug:pk>', views.UserDelete.as_view(), name='user_delete'),
    
    path('donations', views.DonationList.as_view(), name='donation_list'), 
    path('newdonation', views.DonationCreate.as_view(), name='donationtype_create'),
    path('contribute', views.UserView.as_view(), name='user_view'),
    path('donate', views.UserDonate.as_view(), name='user_donate'),
    path('give', views.GiveDonation.as_view(), name='give_donation'),

    path('cart', views.Cart.as_view(), name='cart')
]