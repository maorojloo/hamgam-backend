from django.db import models

# Create your models here.



class Skill(models.Model):
    name = models.CharField(max_length=50, blank=False)

    owner = models.ForeignKey('account.Account', on_delete=models.CASCADE,related_name='skill_owner'  ,blank=True)

    category = models.ForeignKey('idea.Category', on_delete=models.DO_NOTHING,  blank=True)

    sub_category = models.ForeignKey('idea.SubCategory', on_delete=models.DO_NOTHING,  blank=True)

    users = models.ManyToManyField('account.Account',  blank=True, related_name='skill_users')

    ideas = models.ManyToManyField('idea.Idea', blank=True)

    image_link = models.URLField(blank=True, null=True)


