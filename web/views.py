from statistics import mode
from django.shortcuts import render
from  . import models
# Create your views here.

def index(request):
    context = {
        'testimonial':models.Testimonial.objects.all(),
        'products':models.Product.objects.all()
    }
    return render(request,'index.html',context)

def about(request):
    context = {
        'team':models.Team.objects.all()
    }
    return render(request, 'about.html',context)

def blog(request):
    context = {
        'blog':models.blog.objects.all()
    }
    return render(request, 'blog.html',context)

def gallery(request):
    context = {
        'gallery':models.Gallery.objects.all()
    }
    return render(request, 'gallery.html',context)