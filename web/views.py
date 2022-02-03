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
    about = models.about.objects.all()
    aboutBananaDivine = ''
    whyBananaDivine = ''
    vision = ''
    mission = ''
    try:
        for i in about:
            if i.category == 'about banana divine':
                aboutBananaDivine = i.content
            elif i.category == 'why banana divine':
                whyBananaDivine = i.content
            elif i.category == 'vision':
                vision = i.content
            elif i.category == 'mission':
                mission = i.content
    except:
        pass

    context = {
        'team':models.Team.objects.all(),
        'vision':vision,
        'mission':mission,
        'why_banana_divine':whyBananaDivine,
        'about_banana_divine':aboutBananaDivine
    }

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = models.contact()
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        

    return render(request, 'about.html',context,)

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
