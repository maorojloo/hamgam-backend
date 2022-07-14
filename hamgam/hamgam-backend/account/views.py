from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets , filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAccountAdminOrReadOnly
# Internals
from .permissions import UpdateOwnProfile
from . import serializers
from .models import Account



# Create your views here.

class AccountViewSet(viewsets.ModelViewSet):
    '''Handle creating and updating profiles.'''
    serializer_class = serializers.UserProfileSerializer
    queryset = Account.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,IsAccountAdminOrReadOnly)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
    

    def get_queryset(self):
        return self.request.user.accounts.filter(active=True)


class AccountLoginApiView(ObtainAuthToken):
    '''Handle creating accounts authentication tokens!'''
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

