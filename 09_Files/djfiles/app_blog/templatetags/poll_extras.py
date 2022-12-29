from django.contrib.auth.models import User
from django import template

register = template.Library()

@register.filter
def search_user(blog):
    return User.objects.get(Blog=blog).username
