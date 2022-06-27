from rest_framework import serializers
from .models import Account


class UserProfileSerializer(serializers.ModelSerializer):
    '''Serializes a user profile object''' 
    class Meta:
        model = Account
        fields = ('id','email', 'name', 'password', 'phone', 'bio', 'avatar', '','is_staff', 'date_joined','last_login','last_login', 'is_active')
        # we need to make password write only in order for nobody to see  
        extra_kwargs = {
            'password': {
                'write_only':True,
                'style': {'input_type':'password'},
            }
        }
    def create(self,validated_data):
        '''Create and return a new user profile'''
        user = Account.objects.create(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password'],
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password'],
        )
        # it will override the creation of user in order to hash the password.
        return user
