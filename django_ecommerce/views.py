from django.http import JsonResponse
from django.shortcuts import render
from shop.models import Product
from contact.forms import SubscriberForm
from Banner.models import Banner
from Customer.models import Customer


def home_page(request):
    banners = Banner.objects.all().order_by("-id")
    customer = Customer.objects.all()
    products = Product.objects.all()[:8]
    # partner = Partner.objects.all()
    form = SubscriberForm()

    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        "products": products,
        "form": form,
        "banners": banners,
        "customer": customer,
    }
    return render(request, "home.html", context)


