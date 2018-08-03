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

# Create your models here.
