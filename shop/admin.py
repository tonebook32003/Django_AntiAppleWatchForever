from django.contrib import admin
from .models import Category, Product, Thumbnail
from .forms import ProductAdminForm


class ThumbnailInline(admin.TabularInline):
    model = Thumbnail
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = [
        "name",
        "price",
        "category",
        "date",
        "details",
        "photo",
        "date",
        "inventory",
    ]
    inlines = [ThumbnailInline]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if "thumbnails" in request.FILES:
            for image in request.FILES.getlist("thumbnails"):
                Thumbnail.objects.create(product=obj, image=image)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
