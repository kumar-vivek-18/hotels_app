from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils import Choices
# Create your models here.


class User(models.Model):
    GENDER = Choices(
        (1, 'male', _('Male')),
        (2, 'female', _('Female'))
    )
    user_email = models.EmailField(unique=True, verbose_name=_('Email'), help_text=_('Enter a valid email address'))
    user_name = models.CharField(max_length=255, verbose_name=_('Name'), help_text=_('Enter your full name'))
    user_phone = models.CharField(max_length=20,unique=True, verbose_name=_('Phone Number'), help_text=_('Enter your phone number'))
    user_gender = models.IntegerField(choices=GENDER, null=True, verbose_name=_('Gender'))
    user_location = models.CharField(max_length=255, verbose_name=_('Location'), help_text=_('Enter your location'))
    user_profile_image = models.ImageField(upload_to='media/',null=True, blank=True, verbose_name=_('Profile Image'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_name

    class Meta:
        managed = True
        db_table = 'user'
        indexes = [
            models.Index(fields=['user_phone']),
            models.Index(fields=['id'])
        ] 