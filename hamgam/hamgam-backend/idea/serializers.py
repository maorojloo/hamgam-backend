#from asyncore import file_dispatcher
from rest_framework import serializers
from .models import Idea, Comment, Category, SubCategory


class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = '__all__'
