from django.urls import path
from . import views

app_name = 'donation'

urlpatterns = [
    path('', views.UserList.as_view(), name='user_list'),
    path('add', views.UserCreate.as_view(), name='user_create'),
    path('delete/<slug:pk>', views.UserDelete.as_view(), name='user_delete')
]