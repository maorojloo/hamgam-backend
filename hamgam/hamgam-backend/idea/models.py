from venv import create
from django.db import models
from django.urls import reverse
import pytz 
import datetime 
from django.utils import timezone
from account.models import Account
from django.contrib import admin
from django.utils.translation import gettext as _
from config.shared import TimeStampedModel, Postable


class Category(Postable):
	
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name 

	class Meta:
		ordering = ('name', )
		verbose_name = 'تگ'
		verbose_name_plural = 'تگ ها '


class SubCategory(Postable):
	
	name = models.CharField(max_length=50)

	cat = models.ForeignKey(Category, on_delete=models.CASCADE)


	def __str__(self):
		return f'{self.name} in {self.cat}' 

	class Meta:
		ordering = ('name', )
		verbose_name ='زیرتگ '
		verbose_name_plural = 'زیرتگ ها '


class Idea(models.Model):
    
    STATUS_CHOICES = (
    	('draft', 'در حال انتظار'),
    	('published', 'منتشر شده'),
    )
    
    title = models.CharField(max_length=50)

    content = models.TextField()

    creator = models.ForeignKey("account.UserProfile", on_delete=models.CASCADE, related_name='idea_creator')
    
    pub_date = pub_date = models.DateTimeField('published date')
    
    status = models.CharField(max_length=60, choices = STATUS_CHOICES, default='draft', verbose_name='وضعیت')

    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
	
    sub_cat = models.ForeignKey(SubCategory,on_delete=models.CASCADE)

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    


class Comment(TimeStampedModel):
    title = models.CharField(max_length=50)

    content = models.TextField()

    post = models.ForeignKey(Idea, on_delete=models.CASCADE)

    commentor = models.ForeignKey(Account, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={"pk": self.pk})
    