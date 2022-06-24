from re import S
from djangorestframework import serializers
from .models import Skill








class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'