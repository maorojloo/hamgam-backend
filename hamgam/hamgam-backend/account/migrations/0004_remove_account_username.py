# Generated by Django 4.0.5 on 2022-06-27 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_account_options_alter_account_unique_together_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='username',
        ),
    ]
