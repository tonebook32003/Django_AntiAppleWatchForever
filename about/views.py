from django.shortcuts import render
from Customer.models import Customer
from .models import OurTeam


def about_page(request):
    ourteam = OurTeam.objects.all()
    context = {
        "ourteam": ourteam,
    }
    return render(request, "about/about.html", context)
