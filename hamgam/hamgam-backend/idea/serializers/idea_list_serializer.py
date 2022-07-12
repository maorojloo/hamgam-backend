from rest_framework import serializers
from idea.models import Idea , Comment, Category
from skill.serializers import SkillIdeaSerializer
from account.serializers import CreaterIdeaSerializer, JustEmailSerializer
from .cat_serializer import CategorySerializer

class IdeaListSerializer(serializers.ModelSerializer):

    skills = SkillIdeaSerializer(read_only=True, many=True)
    creator = JustEmailSerializer(read_only=True, many=False)
    cat = CategorySerializer(read_only=True, many=True)
    class Meta:
        model = Idea
        fields = ('id', 'title', 'creator','cat', 'skills','likes')
        #exclude = ('cat',)


