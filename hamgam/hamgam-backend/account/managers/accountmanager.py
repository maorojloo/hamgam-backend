from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class AccountManager(BaseUserManager):
	use_in_migrations = True 

	def _create_user(self, email, username, phone,password, **extra_fields):
		values = [email,username, phone]
		field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
		for field_name, value in field_value_map.items():
			if not value: 
				raise ValueError(f'the {field_name} value must be set!')


		email = self.normalize_email(email)
		
		user = self.model(email=email, username=username, phone=phone, **extra_fields)

		user.set_password(password)

		user.save(using=self._db)

		return user 

	def create_user(self, email,username,phone,password=None, **extra_fields):
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, username, phone,password, **extra_fields)

	
	def create_staff(self, email, username, phone, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, username, phone,password, **extra_fields)


	def create_superuser(self, email, username, phone, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		return self._create_user(email, username, phone,password, **extra_fields)
