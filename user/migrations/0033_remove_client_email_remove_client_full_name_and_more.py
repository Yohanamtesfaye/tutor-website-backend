# Generated by Django 5.0.1 on 2024-04-06 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0032_remove_tutor_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='email',
        ),
        migrations.RemoveField(
            model_name='client',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='client',
            name='password',
        ),
        migrations.RemoveField(
            model_name='client',
            name='username',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='full_name',
        ),
    ]
