from django.db import models
# from PIL import Image
# from django.contrib.auth.models import User


class File(models.Model):
    file = models.FileField(upload_to='file')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
