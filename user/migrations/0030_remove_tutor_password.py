# Generated by Django 5.0.1 on 2024-04-05 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0029_tutor_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='password',
        ),
    ]