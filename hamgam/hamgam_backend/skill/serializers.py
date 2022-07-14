from rest_framework import serializers
from .models import Skill
from account.serializers import JustEmailSerializer
#from idea.serializers import IdeaSkillSerializer
from idea.models import Category, Comment, Idea
from account.serializers import CreaterIdeaSerializer, JustEmailSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('updated', 'created', 'active')


class IdeaSkillSerializer(serializers.ModelSerializer):
    creator = CreaterIdeaSerializer(read_only=True, many=False)
    class Meta:
        model = Idea
        fields = ('id', 'title', 'creator')

class SkillIdeaSerializer(serializers.ModelSerializer):
    users = JustEmailSerializer(read_only=True, many=True)
    #ideas = IdeaSkillSerializer(read_only=True, many=True)
    categories = CategorySerializer(read_only=True, many=True)
    class Meta:
        model = Skill
        fields = ('id', 'users', 'name', 'categories')


class SkillDetailSerializer(serializers.ModelSerializer):
    owner = CreaterIdeaSerializer(read_only=True, many=False)
    users = JustEmailSerializer(read_only=True, many=True)
    ideas = IdeaSkillSerializer(read_only=True, many=True)
    categories = CategorySerializer(read_only=True, many=True)
    class Meta:
        model = Skill
        fields = '__all__'

class SkillListSerializer(serializers.ModelSerializer):

    categories = CategorySerializer(read_only=True, many=True)
    class Meta:
        model = Skill
        #fields = '__all__'
        exclude = ('owner', 'users', 'ideas')