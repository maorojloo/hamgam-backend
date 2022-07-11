from venv import create
from django.db import models
import pytz 
import datetime 
from django.utils import timezone
#from user.models import UserModel
from django.contrib import admin
# Create your models here.


class Idea(models.Model):
    

    title = models.CharField(max_length=50)

    content = models.TextField()

    creator = models.ForeignKey("account.UserProfile", on_delete=models.CASCADE, related_name='idea_creator')
    
    pub_date = pub_date = models.DateTimeField('published date')


    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    