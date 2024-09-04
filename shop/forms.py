from django import forms
from .models import Product, Thumbnail
from .widgets import MultipleFileInput


class ProductAdminForm(forms.ModelForm):
    thumbnails = forms.FileField(widget=MultipleFileInput(), required=False)

    class Meta:
        model = Product
        fields = "__all__"
