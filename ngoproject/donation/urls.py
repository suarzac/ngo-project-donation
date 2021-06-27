from django.urls import path
from . import views

app_name = 'donation'

urlpatterns = [
    path('manage', views.UserList.as_view(), name='user_list'),
    path('add', views.UserCreate.as_view(), name='user_create'),
    path('update/<slug:pk>', views.UserUpdate.as_view(), name='user_update'), 
    path('delete/<slug:pk>', views.UserDelete.as_view(), name='user_delete')
]