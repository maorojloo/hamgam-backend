from django.db import models

# Create your models here.



class Skill(models.Model):
    name = models.CharField(max_length=50, blank=False)

    owner = models.ForeignKey('account.Account', on_delete=models.CASCADE)

    category = models.ForeignKey('idea.Category', on_delete=models.DO_NOTHING)

    sub_category = models.ForeignKey('idea.SubCategory', on_delete=models.DO_NOTHING)

    users = models.ManyToManyField('account.Account', on_delete=models.CASCADE, blank=True)

    ideas = models.ManyToManyField('idea.Idea', on_delete=models.CASCADE, blank=True)

    image_link = models.URLField(blank=True, null=True)