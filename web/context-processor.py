from . models import banner

def main_context(request):
    baner = banner.objects.all().first()
    return {
        'domain' : request.META['HTTP_HOST'],
        'banner'  : baner,
    }