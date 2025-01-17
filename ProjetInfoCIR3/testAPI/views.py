from django.http import HttpResponse
from django.conf import settings
import os

def react_view(request):
    filepath = os.path.join(settings.BASE_DIR, 'static/react/dist/index.html')
    with open(filepath, 'r') as file:
        return HttpResponse(file.read(), content_type='text/html')
