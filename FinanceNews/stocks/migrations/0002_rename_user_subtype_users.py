# Generated by Django 3.2.6 on 2021-08-26 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subtype',
            old_name='user',
            new_name='users',
        ),
    ]
