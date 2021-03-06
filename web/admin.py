from email import message
from django.contrib import admin
from . import models
# Register your models here.
class Testimonial(admin.ModelAdmin):
    model = models.Testimonial
    list_display = ['name', 'image','description', 'destination']

admin.site.register(models.Testimonial, Testimonial)

class Banner(admin.ModelAdmin):
    model = models.banner
    list_display = ['heading','content']

admin.site.register(models.banner,Banner)

class Products(admin.ModelAdmin):
    model = models.Product
    list_display = ['name', 'image','description', 'price']

admin.site.register(models.Product, Products)


class Gallery(admin.ModelAdmin):
    model = models.Gallery
    list_display = ['image']

admin.site.register(models.Gallery, Gallery)

class Team(admin.ModelAdmin):
    model = models.Team
    list_display = ['name','image','description','facebook','twiter','instagram']

admin.site.register(models.Team, Team)

class Blog(admin.ModelAdmin):
    model = models.blog
    list_display = ['heading','image','category','content']

admin.site.register(models.blog,Blog)

class Contact(admin.ModelAdmin):
    model = models.contact
    list_display = ['date','name','email','subject','message']

admin.site.register(models.contact,Contact)

class Background_image(admin.ModelAdmin):
    model = models.background_image
    list_display = ['id','image_one','image_two','image_three']

admin.site.register(models.background_image,Background_image)


class About_us(admin.ModelAdmin):
    model = models.about
    list_display = ['category','content']

admin.site.register(models.about,About_us)