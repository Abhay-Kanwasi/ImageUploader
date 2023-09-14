from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    image = models.ImageField(upload_to = "uploaded_images")
    date = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null= True, blank=True)
