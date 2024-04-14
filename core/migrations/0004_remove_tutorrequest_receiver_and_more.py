# Generated by Django 5.0.4 on 2024-04-13 18:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_clientnotification_is_approved_and_more'),
        ('user', '0036_tutor_subject'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorrequest',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='tutorrequest',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='tutorrequest',
            name='status',
        ),
        migrations.AddField(
            model_name='tutorrequest',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.client'),
        ),
        migrations.AddField(
            model_name='tutorrequest',
            name='tutor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.tutor'),
        ),
        migrations.CreateModel(
            name='CompletedJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('completed_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.client')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.tutor')),
            ],
        ),
        migrations.CreateModel(
            name='OngoingJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.client')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.tutor')),
            ],
        ),
        migrations.CreateModel(
            name='TutorRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('date_rated', models.DateTimeField(auto_now_add=True)),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.tutor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]