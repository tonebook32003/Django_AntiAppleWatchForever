from django.urls import path
from . import views, include

urlpatterns = [
    path("", views.Product_Banner, name="product_banner"),
    path("ckeditor/", include("ckeditor_uploader.urls")),
]
