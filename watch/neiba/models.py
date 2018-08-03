from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from location_field.models.plain import PlainLocationField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
"""This is the class model for the members in the neighbourhood"""
class NeighbourHood(models.Model):
    name = models.CharField(max_length =30)
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    occupants = models.IntegerField()

    def __str__(self):
        return self.name

    def save_neigbourhood(self):
        self.save()

    def delete_neigbourhood(self):
        self.delete()
    @classmethod
    def find_neigbourhood(cls):
        neiba = NeighbourHood.objects.all()
        return naiba

    @classmethod
    def update_neigbourhood(cls):
        update_neiba = NeighbourHood.objects.all()
        return update_neiba

    @classmethod
    def update_occupants(cls,occupants):
        neibas = cls.objects.update(occupants=occupants).all()
        return neibas

"""class model that represent the users who log init the app"""
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    email = models.EmailField()
    gender = models.CharField(max_length=1,choices=(('M','Male'),('F','Female')),blank=True)
    house = models.CharField(max_length=200)
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    contribution=models.CharField(max_length=200)
    photo = models.ImageField(upload_to = 'users/%Y/%m/%d', null=True)

    last_update = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

    def save_profile(self):
        self.save()
