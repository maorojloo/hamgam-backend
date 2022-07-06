from rest_framework import serializers
from . import models


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shop
        fields = [
            'account_id',
            'idea_id',
            'address',
            'content',
            'resume_link',
            'active',
            'objects',
        ]

    def validate_content(self, value):
        if len(value) < 25:
            raise serializers.ValidationError(F"{value} is too short")
        return value
