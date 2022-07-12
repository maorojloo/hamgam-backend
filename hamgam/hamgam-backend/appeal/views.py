from asyncio import events
from rest_framework import response
from . import models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http.response import JsonResponse
from django.http import HttpResponse, Http404


class appealAPIView(APIView):

    # get -> read
    # post -> create
    # put -> update
    # delete -> delete

    def get_object(self, pk):
        try:
            return models.Petition.objects.get(pk=pk)
        except models.Petition.DoesNotExist:
            raise Http404

    # read

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = serializers.AppealSerializer(data)

        else:
            data = models.Petition.objects.all()
            serializer = serializers.AppealSerializer(data, many=True)

        return Response(serializer.data)

    # create

    def post(self, request, format=None):
        data = request.data
        serializer = serializers.AppealSerializer(data=data)

        # Check if the data passed is valid
        serializer.is_valid(raise_exception=True)

        # Create Todo in the DB
        serializer.save()

        # Return Response to User

        response = Response()

        response.data = {
            'message': 'added Created Successfully',
            'data': serializer.data
        }

        return response

    def put(self, request, pk=None, format=None):
        # update
        Petition_update = self.get_object(pk)

        serializer = serializers.AppealSerializer(
            instance=Petition_update, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()

        response.data = {
            'message': 'Todo Updated Successfully',
            'data': serializer.data
        }

        return response

    def delete(self, request, pk, format=None):
        # delete
        Petition_delete = self.get_object(pk)
        Petition_delete.delete()
        return Response({'message': 'Todo Deleted Successfully'})
