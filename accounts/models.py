from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='clients_profile_image', blank=True, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return user.username


class Astrologer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=25, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    experience = models.CharField(max_length=25, blank=True, null=True)
    qualificatons = models.CharField(max_length=25, blank=True, null=True)
    languages = models.CharField(max_length=25, blank=True, null=True)
    profile_image = models.ImageField(upload_to='astrologers_profile_image', blank=True, null=True)
    certificates = models.FileField(upload_to='certificate', blank=True, null=True)

    CONSULTANCY_TYPES = (
        ('Astrology', 'Astrology'),
        ('Numerology', 'Numerology'),
        ('Palmistry', ' Palmistry'),
        ('Facereading', 'Facereading'),
        ('Tarot reading', 'Tarot reading'),
        ('Feng shui', 'Feng shui'),
        ('Tarot', 'Tarot'),
        ('Reiki crystal ', 'Reiki crystal '),
        ('Pranic healing', 'Pranic healing'),
        ('Other', 'Other')
    )
   

    consultancy_types = models.CharField(
        max_length=100,
        choices=CONSULTANCY_TYPES,
        blank=True,
        default='Other',
    )



    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return user.username
