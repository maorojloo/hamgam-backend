# Generated by Django 4.0.6 on 2022-07-09 04:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('idea', '0002_idea_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='Petition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='ساخت')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='انتشار')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='آپدیت')),
                ('content', models.TextField(max_length=255)),
                ('resume_link', models.URLField()),
                ('active', models.BooleanField(default=True)),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Petitions', to=settings.AUTH_USER_MODEL)),
                ('idea_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Petitions', to='idea.idea')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
