from django.db import models
from django.urls import reverse
import datetime 
from django.utils import timezone
from account.models import Account
from .idea import Idea
from django.contrib import admin
from django.utils.translation import gettext as _
from config.shared import TimeStampedModel, Postable

class Comment(TimeStampedModel):
    title = models.CharField(max_length=50)

    content = models.TextField()

    post = models.ForeignKey(Idea, on_delete=models.CASCADE)

    commentor = models.ForeignKey(Account, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={"pk": self.pk})
    