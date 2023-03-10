"""Module for all methods"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers,status
from dialinginapi.models import MethodEquipment, Method

class MethodEquipmentView(ViewSet):
    """Class create viewset for MethodEquipment"""
    def list(self, request):
        """Handles GET requests to get all method_equipment """
        method_equipment = MethodEquipment.objects.all()

        try:
            method = request.query_params.get('methodId')
            method_equipment = method_equipment.filter(method_id = method)
            serializer = MethodEquipmentSerializer(method_equipment, many=True)

            return Response(serializer.data)
        except Method.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

class MethodEquipmentSerializer(serializers.ModelSerializer):
    """Serilizer for Method Class"""
    class Meta:
        model = MethodEquipment
        fields = (
          'id',
          'type',
          'name',
          'method_id',
        )
