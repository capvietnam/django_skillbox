from django.http import Http404

from app_news.models import News
from app_users.models import Profile


class UserRequiredMixin:
    def has_permissions(self):
        return Profile.objects.filter(user=self.request.user).values('can_news')[0]['can_news'] == True

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            raise Http404
        return super().dispatch(request, *args, **kwargs)

