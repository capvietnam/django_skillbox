from django.core.exceptions import PermissionDenied
from datetime import datetime

print(datetime.now())

class first_middleware:

    def __init__(self, get_respons):
        self._get_respons = get_respons

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        url = request.META.get('PATH_INFO')
        http = request.META.get('HTTP_HOST')

        with open('log.txt', 'a') as file:
            file.write(str(f'time: {datetime.now()}\tip: {ip},\t url: {url},\t HTTP: {http}'))

        respons = self._get_respons(request)
        return respons

