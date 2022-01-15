from statistics import mode
from turtle import heading
from django.db import models
from versatileimagefield.fields import VersatileImageField, PPOIField

# Create your models here.


class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to ='testimonial')
    destination = models.CharField(max_length=50,null=True,blank=True)

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to ='Product')

class Gallery(models.Model):
    image = VersatileImageField(upload_to = 'gallery',ppoi_field='image_ppoi')
    image_ppoi = PPOIField()

class Team(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to ='team')
    description = models.TextField(max_length=300)
    facebook = models.URLField(max_length=100,null=True,blank=True)
    twiter = models.URLField(max_length=100,null=True,blank=True)
    instagram = models.URLField(max_length=100,null=True,blank=True)


class blog(models.Model):
    heading = models.CharField(max_length=100)
    image = VersatileImageField(upload_to = 'blog',ppoi_field='image_ppoi')
    image_ppoi = PPOIField()
    date = models.DateField(auto_now=True)
    category = models.CharField(max_length=50,null=True,blank=True)
    content = models.TextField(max_length=10000)

class banner(models.Model):
    heading = models.CharField(max_length=100)
    content = models.TextField(max_length=200,null=True,blank=True)