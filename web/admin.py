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