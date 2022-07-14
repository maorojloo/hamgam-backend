from rest_framework import serializers
from .models import Account 


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        #fields = ('id','email', 'name', 'password', 'phone', 'bio', 'avatar', 'is_staff', 'date_joined','last_login','last_login', 'is_active')
        exclude = ('is_staff', 'date_joined', 'last_login')
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
        )
        # it will override the creation of user in order to hash the password.
        return user




class CreaterIdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        #fields = ('id','email', 'name', 'password', 'phone', 'bio', 'avatar', 'is_staff', 'date_joined','last_login','last_login', 'is_active')
        exclude = ('is_staff', 'date_joined', 'last_login', 'password', 'is_superuser', 'groups', 'user_permissions')
    


class JustEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id','email', 'avatar')
        
#
#class LikeSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Account
#        fields = ('likes')