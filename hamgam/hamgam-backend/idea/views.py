from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status, filters 
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import ModelViewSet

#  Internals 
from .serializers import IdeaSerializer
from .models import Idea  


class IdeaViewSet(ModelViewSet):
    serializer_class = IdeaSerializer
    queryset = Idea.objects.all()
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('content', 'title',)


 #sqlalchemy schedule redis requests selenium selenium-wire pytz streamlink ffmpeg ffmpeg-python ffprobe ffprobe-python pydub deepspeech webdriver-manager