from django.urls import path
from .views import shop_page, search_product, product_details, wishlist

urlpatterns = [
    path("", shop_page, name="shop"),
    path("search/", search_product, name="search"),
    path("product/<int:product_id>/", product_details, name="product-details"),
    path("wishlist/", wishlist, name="wishlist"),
]
