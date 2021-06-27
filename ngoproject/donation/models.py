from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None, is_staff=False, is_admin=False, is_active=True):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        if not first_name:
            raise ValueError("Users must have a first name")            
        user_obj = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self.db)

        return user_obj

    def create_staffuser(self, first_name, last_name, email, password=None):
        user = self.create_user(
            first_name,
            last_name,
            email,
            password=password,
            is_staff= True,
            is_active= True
        )
        return user
    
    def create_superuser(self, first_name, last_name, email, password=None):
        user = self.create_user(
            first_name,
            last_name,
            email,
            password=password,
            is_staff=True,
            is_admin= True
        )
        return user

class User(AbstractBaseUser):
    ROLE_OPTS = [('ADMIN', 'Admin'), ('USER', 'User')]

    first_name = models.CharField(default='', max_length=255, blank=True, null=True)
    last_name = models.CharField(default='', max_length=255, blank=True, null=True)
    email = models.EmailField(default = '',max_length=255, unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=True)
    admin = models.BooleanField(default=True)

    role_opt = models.CharField('role', max_length=5, choices=ROLE_OPTS, default='User')
    USERNAME_FIELD = 'email' #username

    
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role_opt']
    
    objects = UserManager()

    def __str__(self):
        return self.email
    def get_full_name(self):
        return self.email
    def get_short_name(self):
        return self.email

    # permissions 
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff
    @property
    def is_admin(self):
        return self.admin
    @property
    def is_active(self):
        return self.active

'''
class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_OPTS = [('ADMIN', 'Admin'), ('USER', 'User')]
    id = models.BigAutoField(primary_key=True)
    
    first_name = models.CharField(default = '', max_length=200)
    last_name = models.CharField(default='', max_length=200)

    password = models.CharField(default = '', max_length=200)

    role_opt = models.CharField('role', max_length=5, choices=ROLE_OPTS, default='User')
    
    def __str__(self):
        return self.first_name
    def get_absolute_url(self):
        return reverse("User", kwargs={"pk": self.pk})
'''

class Donation(models.Model):
    first_name = models.CharField(default = '', max_length=25)
    last_name = models.CharField(default='', max_length=25)
    
    cell_num = models.CharField(default='', max_length=14, blank=True)
    phone_num = models.CharField('phone #', default='', max_length=14, blank=True) 
    usr_email = models.EmailField('email address', default= '', max_length=200)

    usr_addr1 = models.CharField('address 1', max_length=50)
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
