"""Module for all methods"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from dialinginapi.models import Grind

class GrindView(ViewSet):
    """Class create viewset for Method"""
    def retrieve(self, request,pk):
        """Get single method, method"""
        try:
            grind = Grind.objects.get(pk=pk)
            serilaizer = GrindSerializer(grind)

            return Response(serilaizer.data)
        except Grind.DoesNotExist as ex:

            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handles GET requests to get all methods"""
        grinds = Grind.objects.all().order_by('order')
        serializer = GrindSerializer(grinds, many=True)

        return Response(serializer.data)

class GrindSerializer(serializers.ModelSerializer):
    """Serilizer for Method Class"""
    class Meta:
        model = Grind
        fields = (
          'id',
          'grind_size',
          'image_url',
          'order',
        )
