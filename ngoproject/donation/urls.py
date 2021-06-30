from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'donation'

urlpatterns = [
    path('manage', views.UserList.as_view(), name='user_list'),
    path('add', views.UserCreate.as_view(), name='user_create'),
    path('update/<slug:pk>', views.UserUpdate.as_view(), name='user_update'), 
    path('delete/<slug:pk>', views.UserDelete.as_view(), name='user_delete'),
    
    path('donations', views.DonationList.as_view(), name='donation_list'), 
    path('newdonationtype', views.DonationCreateType.as_view(), name='donationtype_create'),

    path('contribute', views.UserView.as_view(), name='user_view'),
    path('donate/<slug:slug>', views.UserDonate.as_view(), name='user_donate'),
   

    path('cart', views.Cart.as_view(), name='cart')
]