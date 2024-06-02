# admin.py

from django.contrib import admin
from .models import Banner


class BannerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "description",
        "image",
        "created_at",
    ) 


admin.site.register(Banner, BannerAdmin)
