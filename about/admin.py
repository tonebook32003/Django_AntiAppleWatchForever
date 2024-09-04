from django.contrib import admin
from .models import OurTeam


# Register your models here.
class OurTeamAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "image",
        "created_at",
    )


admin.site.register(OurTeam, OurTeamAdmin)
