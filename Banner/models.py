# models.py

from django.db import models


class Banner(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()  # Ensure this matches the field name
    image = models.ImageField(upload_to="banners/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
