# Generated by Django 3.2.6 on 2021-08-27 09:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stocks', '0003_auto_20210827_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocknews',
            name='users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
