from django.db import models

# Create your models here.

from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy

# Create your models here.

class User(models.Model):
    ROLE_OPTS = [('ADMIN', 'Admin'), ('USER', 'User')]
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    first_name = models.CharField(default = '', max_length=200)
    last_name = models.CharField(default='', max_length=200)

    usr_email = models.EmailField(default= '', max_length=200)
    usr_password = models.CharField(max_length=200)

    role_opt = models.CharField( max_length=5, choices=ROLE_OPTS, default='User')
    
    def __str__(self):
        return self.first_name
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    

class Donation(models.Model):
    first_name = models.CharField(default = '', max_length=25)
    last_name = models.CharField(default='', max_length=25)
    
    cell_num = models.CharField(default='', max_length=14, blank=True)
    phone_num = models.CharField(default='', max_length=14, blank=True) 
    usr_email = models.EmailField(default= '', max_length=200)

    usr_addr1 = models.CharField(max_length=50)
    usr_addr2 = models.CharField(max_length=50, blank=True)
    usr_city = models.CharField(default = '', max_length=50, blank=True)
    usr_state = models.CharField(default = '', max_length=50)
    usr_zip = models.IntegerField(default='')
    usr_country = models.CharField(default = '', max_length=50)

    urbanization = models.CharField(default = '', max_length=50)

    donation_amount = models.IntegerField(default = '')

    def __str__(self):
        return self.last_name
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
class Cart(models.Model):
    pass
