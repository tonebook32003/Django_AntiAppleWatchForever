from django.shortcuts import render
from .models import Customer


# Create your views here.
def Customer_Review(request):
    customers = Customer.objects.all()

    return render(request, "home.html", customers)
