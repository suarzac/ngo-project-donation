from django.contrib import admin
from .models import User, Donation

# Register your models here.
admin.site.register(User)
admin.site.register(Donation)