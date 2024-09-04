from django.db import models


# Create your models here.
class OurTeam(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()  # Ensure this matches the field name
    image = models.ImageField(upload_to="ourteam/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
