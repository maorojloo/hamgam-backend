from xml.etree.ElementTree import Comment
from django.db import models
from django.urls import reverse
import datetime 
from django.utils import timezone
from account.models import Account
from django.contrib import admin
from django.utils.translation import gettext as _
from config.shared import TimeStampedModel, Postable
from.comment import Comment
from .category import Category
#from .sub_category import SubCategory
from skill.models import Skill

class Idea(models.Model):
    
    STATUS_CHOICES = (
    	('draft', 'در حال انتظار'),
    	('published', 'منتشر شده'),
    )
    
    title = models.CharField(max_length=50)

    content = models.TextField()

    creator = models.ForeignKey("account.Account", on_delete=models.CASCADE, related_name='idea_creator')
    
    pub_date  = models.DateTimeField('published date')
    
    status = models.CharField(max_length=60, choices = STATUS_CHOICES, default='draft', verbose_name='وضعیت')

    cat = models.ManyToManyField(Category, related_name='idea_cats')
	
    #sub_cat = models.ManyToManyField(SubCategory)
    
    comment = models.ForeignKey(Comment, default='1' ,on_delete=models.CASCADE)
    
    likes = models.ManyToManyField(Account, related_name='idea_likes')

    skills = models.ManyToManyField(Skill, related_name='idea_skills')

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='به تازگی منتشر شده بود؟',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    