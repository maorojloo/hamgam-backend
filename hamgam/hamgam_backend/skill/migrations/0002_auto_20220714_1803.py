# Generated by Django 3.2.14 on 2022-07-14 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0004_rename_comment_idea_comments'),
        ('skill', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='category',
        ),
        migrations.AddField(
            model_name='skill',
            name='categories',
            field=models.ManyToManyField(blank=True, to='idea.Category'),
        ),
    ]
