from django.db import models
from django.contrib.auth.models import User
from django.apps import apps

Comment = apps.get_model('app_news', 'Comment')

Comment['user'] = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='comments',
                                    verbose_name='Пользователь')
