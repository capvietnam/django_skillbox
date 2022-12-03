from django.contrib.auth.models import User
from django.db import models
# from app_media.models


class Blog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='blog')
    description = models.CharField(max_length=500)
    file = models.FileField()

    def __str__(self):
        return self.user.name
