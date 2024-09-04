from django.urls import path
from . import views

urlpatterns = [
    path("", views.cart_page, name="cart"),
    path("checkout", views.checkout, name="checkout"),
    # path("add-to-cart", views.add_to_cart, name="add_to_cart"),
]
