from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . models import Account
from .forms import UserCreationForm, UserChangeForm




admin.site.register(Account)

