from django.urls import path
from . import views, include

urlpatterns = [
    path("", views.Customer_Review, name="customer_review"),
    path("ckeditor/", include("ckeditor_uploader.urls")),
]
