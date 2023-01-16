"""Module for all methods"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers,status
from dialinginapi.models import MethodEquipment, Method

class MethodEquipmentView(ViewSet):
    """Class create viewset for Method"""
    def list(self, request):
        """Handles GET requests to get all methods"""
        method_equipment = MethodEquipment.objects.all()

        try:
            method_id = request.query_params.get('methodId')
            method_id = Method.objects.get(pk=method_id)
            if method_id is not None:
                method_equipment = method_equipment.filter(method_id = method_id)
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
