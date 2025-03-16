# Generated by Django 5.1.7 on 2025-03-13 16:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_profileImage',
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Profile Image'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_email',
            field=models.EmailField(help_text='Enter a valid email address', max_length=254, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_gender',
            field=models.IntegerField(choices=[(1, 'Male'), (2, 'Female')], null=True, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_location',
            field=models.CharField(help_text='Enter your location', max_length=255, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(help_text='Enter your full name', max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_phone',
            field=models.CharField(help_text='Enter your phone number', max_length=20, verbose_name='Phone Number'),
        ),
    ]
