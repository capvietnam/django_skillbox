from django.http import Http404


class UserRequiredMixin:
    def has_permissions(self):
        return self.request.user.profile.can_news

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            raise Http404
        return super().dispatch(request, *args, **kwargs)


