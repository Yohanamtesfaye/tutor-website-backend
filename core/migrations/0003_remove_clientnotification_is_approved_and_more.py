# Generated by Django 5.0.1 on 2024-04-07 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_clientnotification_is_approved_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientnotification',
            name='is_approved',
        ),
        migrations.RemoveField(
            model_name='clientnotification',
            name='is_declined',
        ),
    ]