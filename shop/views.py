from django.http import JsonResponse
from django.shortcuts import render
from .models import Category, Product


def shop_page(request):
    category = Category.objects.all()
    selected_category = request.GET.get("category")

    if selected_category:
        products = Product.objects.filter(category_id=selected_category, is_draft=False)
    else:
        products = Product.objects.filter(is_draft=False)

    context = {
        "category": category,
        "products": products,
    }

    return render(request, "shop/shop.html", context)


def search_product(request):
    query = request.GET.get("q")
    if query:
        # Search for products whose name contains the query
        products = Product.objects.filter(
            name__icontains=query, is_draft=False
        ).order_by("name")
    else:
        # If no query is provided, return all products
        products = Product.objects.filter(is_draft=False).order_by("name")

    # Include categories for the sidebar menu
    categories = Category.objects.all()

    return render(
        request, "shop/shop.html", {"products": products, "category": categories}
    )


def product_details(request, product_id):
    product_details = Product.objects.get(id=product_id)
    ctg = Category.objects.get(name=product_details.category)
    related_products = Product.objects.filter(category=ctg)
    context = {"product": product_details, "related_products": related_products}
    return render(request, "shop/product-details.html", context)


def wishlist(request):
    return render(request, "shop/wishlist.html")



