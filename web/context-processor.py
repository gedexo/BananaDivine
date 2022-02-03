from . models import banner,background_image

def main_context(request):
    baner = banner.objects.all().first()
    images = background_image.objects.all().first()
    return {
        'domain' : request.META['HTTP_HOST'],
        'banner'  : baner,
        'images': images,
    }