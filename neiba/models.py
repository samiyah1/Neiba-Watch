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


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    NeighbourHood = models.ForeignKey(NeighbourHood, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    postDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-postDate']

    def save_post(self):
        self.save()

class Join(models.Model):
    '''
    Model that keeps track of users and the neighbourhoods they're in
	'''
    user_id = models.ForeignKey(User)
    hood_id = models.ForeignKey(NeighbourHood)

    def __str__(self):
        return self.user_id

class Social(models.Model):
    socialName = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    NeighbourHood = models.ForeignKey(NeighbourHood, null=True)

    def __str__(self):
        return self.socialName

class Business(models.Model):
    business_name = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description_of_biz = models.TextField(null=True)
    location = models.CharField(max_length=1000, null=True)
    email = models.EmailField(max_length=254)

    hood = models.ForeignKey(NeighbourHood, null=True)

    @classmethod
    def search_by_business_name(cls, search_term):
        business = cls.objects.filter(business_name__icontains=search_term)
        return business

    def __str__(self):
        return self.business_name

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()
