from django.shortcuts import render
from .models import Banner


# Create your views here.
def Product_Banner(request):
    get_banner = Banner.objects.all()

    return render(request, "home.html", get_banner)
