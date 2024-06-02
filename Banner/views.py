from django.shortcuts import render
from .models import Banner


# Create your views here.
def Product_Banner(request):
    banner = Banner.objects.all()
    context = {"banner": banner}

    return render(request, "shop/shop.html", context)
