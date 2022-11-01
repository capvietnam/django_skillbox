from django import template
from app_users.models import *


register = template.Library()

def profile():
    return Profile.objects.all()

print(profile)