from django.db import models
from ..managers import AccountManager
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.utils import timezone 
from django.urls import reverse, reverse_lazy
# Create your models here.

class Account(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique=True)
	username = models.CharField(max_length=40, unique=True)
	phone = models.CharField(max_length=50)
	bio = models.CharField(max_length=140, blank=True, default='')
	# date_of_birth = models.DateField(blank=True, null=True)
	avatar = models.ImageField(blank=True, null=True)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	date_joined = models.DateTimeField(default=timezone.now)
	last_login = models.DateTimeField(null=True)
	# Do apply this with IP as well 
	address = models.CharField(max_length=250)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	postal_code = models.CharField(max_length=20)
	city = models.CharField(max_length=100)
	
	objects = AccountManager()
	# USERNAME_FIELD is the name of the field on the user model that is used as the unique identifier.
	USERNAME_FIELD = 'email'
	# REQUIRED_FIELDS are the mandatory fields other than the unique identifier
	REQUIRED_FIELDS = ['username', 'phone']


# https://dev.to/joshwizzy/customizing-django-authentication-using-abstractbaseuser-llg
	class Meta:
		unique_together = ('email', 'username', 'phone')

	def __str__(self):
		return f'@{self.username}'

	def get_short_name(self):
		return self.username

	def get_absolute_url(self):
		return reverse("account:profile_detail", kwargs={"pk": self.pk})


        
        	
	#class Meta:
	#	abstract = True 