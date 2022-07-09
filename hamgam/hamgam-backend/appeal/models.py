from django.db import models
from config import shared
# Create your models here.


class Petition(shared.TimeStampedModel):

    account_id = models.ForeignKey(
        "account.Account", on_delete=models.CASCADE, related_name='Petitions')
    idea_id = models.ForeignKey(
        "idea.Idea", on_delete=models.CASCADE, related_name='Petitions')
    content = models.TextField(max_length=255)
    resume_link = models.URLField()
    active = models.BooleanField(default=True)

    objects = shared.ActiveManager()
