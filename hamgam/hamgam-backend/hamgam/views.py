from django.urls import get_resolver
from django.http import HttpResponse

def mamad(request):
    return HttpResponse(get_resolver().url_patterns)