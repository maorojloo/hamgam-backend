from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status, filters 
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#from rest_framework.views import ModelViewSet

from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework import generics
from .serializers import IdeaListSerializer, IdeaDetailSerializer, IdeaUpdateSerializer
from .models import Idea  


class ListIdea(generics.ListAPIView):
    queryset = Idea.objects.filter(status='published')
    serializer_class = IdeaListSerializer


class DetailIdea(generics.RetrieveAPIView):
    queryset = Idea.objects.filter(status='published')
    serializer_class = IdeaDetailSerializer


class UpdateIdea(generics.UpdateAPIView):
    queryset = Idea.objects.filter(status='published')
    serializer_class = IdeaUpdateSerializer


class DeleteIdea(generics.DestroyAPIView):
    queryset = Idea.objects.filter(status='published')
    serializer_class = IdeaDetailSerializer



@api_view(['GET', 'POST', "DELETE"])
def idea_list(request):
    '''
    Get list of idea 
    Post a new Idea 
    Delete All Ideas
    '''
    if request.method == 'GET':
        ideas = get_list_or_404(Idea)
        # Use a more khafan way to search 
        title = request.GET.get('title', None)
        if title is not None:
            ideas = ideas.filter(title__icontains=title)
        ideas_serializer = IdeaListSerializer(ideas, many=True)
        
        return JsonResponse(ideas_serializer.data, safe=False)

    elif request.method == 'POST':
         # validating for already existing data
        if Idea.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This data already exists')
            idea_data = JSONParser().parse(request)
            idea_serializer = IdeaSerializer(data=idea_data)
            if idea_serializer.is_valid():
                idea_serializer.save()
                return JsonResponse(idea_serializer.data, status=status.HTTP_201_CREATED) 
            return JsonResponse(idea_serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE'])
def idea_detail(request, pk):
    # find idea by pk (id)
    idea = get_object_or_404(Idea, pk = pk)
    if request.method == 'GET': 
        try: 
            idea = Idea.objects.get(pk=pk)
             
            idea_serializer = IdeaDetailSerializer(idea)
            return JsonResponse(idea_serializer.data) 
            
        except Idea.DoesNotExist: 
            return JsonResponse({'message': 'ایده شما یافت نشد '}, status=status.HTTP_404_NOT_FOUND) 
 
    elif request.method == 'PUT': 
        idea_data = JSONParser().parse(request) 
        idea_serializer = IdeaDetailSerializer(idea, data=idea_data) 
        if idea_serializer.is_valid(): 
            idea_serializer.save() 
            return JsonResponse(idea_serializer.data) 
        return JsonResponse(idea_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        idea.delete() 
        return JsonResponse({'message': 'ایده با موفقیت دیلیت شد !'}, status=status.HTTP_204_NO_CONTENT)
            

"""class IdeaViewSet(ModelViewSet):
    serializer_class = IdeaListSerializer
    queryset = Idea.objects.all()
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('content', 'title',)
"""

@api_view(['GET'])
def idea_list_published(request):
    # GET all published ideas
    ideas = Idea.objects.filter(published=True)
        
    if request.method == 'GET': 
        ideas_serializer = IdeaListSerializer(ideas, many=True)
        return JsonResponse(ideas_serializer.data, safe=False)
