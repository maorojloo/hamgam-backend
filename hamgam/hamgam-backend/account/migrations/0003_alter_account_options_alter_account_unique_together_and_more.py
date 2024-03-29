# Generated by Django 4.0.5 on 2022-06-27 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_account_is_verified'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterUniqueTogether(
            name='account',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='account',
            name='email_verification_token',
        ),
        migrations.RemoveField(
            model_name='account',
            name='forget_password_token',
        ),
    ]
