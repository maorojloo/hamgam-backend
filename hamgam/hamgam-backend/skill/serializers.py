from rest_framework import serializers
from .models import Skill
from account.serializers import JustEmailSerializer




class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'






class SkillIdeaSerializer(serializers.ModelSerializer):
    users = JustEmailSerializer(read_only=True, many=True)
    class Meta:
        model = Skill
        fields = ('id', 'users', 'name', 'image_link')

