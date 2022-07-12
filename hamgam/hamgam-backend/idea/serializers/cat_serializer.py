from rest_framework import serializers
from idea.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        #fields = '__all__'
        exclude = ('updated', 'created', 'active')


