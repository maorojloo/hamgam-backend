from django.db import models
from ..managers import AccountManager
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.utils import timezone 
from django.urls import reverse, reverse_lazy

from authemail.models import EmailUserManager, EmailAbstractUser

# Create your models here.

class Account(EmailAbstractUser):
	email = models.EmailField(unique=True)
	bio = models.CharField(max_length=140, blank=True, default='')
	# date_of_birth = models.DateField(blank=True, null=True)
	avatar = models.ImageField(blank=True, null=True)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_verified  = models.BooleanField(default=False)
	date_joined = models.DateTimeField(default=timezone.now)
	last_login = models.DateTimeField(null=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)



	objects = EmailUserManager()
	USERNAME_FIELD = 'email'

# https://dev.to/joshwizzy/customizing-django-authentication-using-abstractbaseuser-llg

	def __str__(self):
		return f'{self.email}'

	def get_short_name(self):
		return self.first_name



class ForgetPassword(models.Model):
    user = models.ForeignKey(Account , on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=200 ,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.email
