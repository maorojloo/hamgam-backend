from rest_framework import serializers
from idea.models import Category, Comment, Idea
from skill.serializers import SkillIdeaSerializer
from account.serializers import CreaterIdeaSerializer, JustEmailSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('updated', 'created', 'active')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        #exclude = ('updated', 'created', 'active')

class IdeaSkillSerializer(serializers.ModelSerializer):
    creator = CreaterIdeaSerializer(read_only=True, many=False)
    class Meta:
        model = Idea
        fields = ('id', 'title', 'creator')
        #exclude = ('updated', 'created', 'active')

class IdeaUpdateSerializer(serializers.ModelSerializer):
    skills = SkillIdeaSerializer(read_only=True, many=True)
    #creator = CreaterIdeaSerializer(read_only=True, many=False)
    #cat = CategorySerializer(read_only=True, many=True)
    likes = JustEmailSerializer(read_only=True, many=True)
    class Meta:
        model = Idea
        #fields = '__all__'
        exclude = ('creator','comments', 'likes',)



class IdeaListSerializer(serializers.ModelSerializer):

    skills = SkillIdeaSerializer(read_only=True, many=True)
    creator = JustEmailSerializer(read_only=True, many=False)
    cat = CategorySerializer(read_only=True, many=True)
    class Meta:
        model = Idea
        fields = ('id', 'title', 'creator','cat', 'skills','likes')
        #exclude = ('cat',)



class IdeaDetailSerializer(serializers.ModelSerializer):
    skills = SkillIdeaSerializer(read_only=True, many=True)
    creator = CreaterIdeaSerializer(read_only=True, many=False)
    users = JustEmailSerializer(read_only=True, many=True)
    cat = CategorySerializer(read_only=True, many=True)
    likes = JustEmailSerializer(read_only=True, many=True)
    comments = CommentSerializer(read_only=True, many=True)
    class Meta:
        model = Idea
        fields = '__all__'
        #exclude = ('cat',)


