from .models import Skill 
from .serializers import SkillSerializer
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response


class SkillViewCreate(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

