from rest_framework import serializers
from . import models


class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Petition
        fields = "__all__"

    def validate_content(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(F"{value} is too short")
        return value

