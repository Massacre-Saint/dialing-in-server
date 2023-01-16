"""Module for all methods"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from dialinginapi.models import Method

class MethodView(ViewSet):
    """Class create viewset for Method"""
    def retrieve(self, request,pk):
        """Get single method, method"""
        try:
            method = Method.objects.get(pk=pk)
            serilaizer = MethodSerializer(method)

            return Response(serilaizer.data)
        except Method.DoesNotExist as ex:

            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handles GET requests to get all methods"""
        methods = Method.objects.all()
        serializer = MethodSerializer(methods, many=True)

        return Response(serializer.data)
class MethodSerializer(serializers.ModelSerializer):
    """Serilizer for Method Class"""
    class Meta:
        model = Method
        fields = (
          'id',
          'image_url',
          'description',
          'name',
          'dose_min',
          'dose_max',
          'weight_max',
        )
