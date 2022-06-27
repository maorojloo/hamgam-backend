from django.db import models
from django.urls import reverse
import datetime 
from django.utils import timezone
from account.models import Account
from django.contrib import admin
from django.utils.translation import gettext as _
from config.shared import TimeStampedModel, Postable
from .category import Category

class SubCategory(Postable):
	
	name = models.CharField(max_length=50)

	cat = models.ManyToManyField(Category)


	def __str__(self):
		return f'{self.name} in {self.cat}' 

	class Meta:
		ordering = ('name', )
		verbose_name ='زیرتگ '
		verbose_name_plural = 'زیرتگ ها '
