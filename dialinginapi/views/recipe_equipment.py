"""Module for all methods"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers,status
from dialinginapi.models import RecipeEquipment

class RecipeEquipmentView(ViewSet):
    """Class creates viewset for RecipeEquipment"""
    def retrieve(self, request, pk):
        """Handles GET requests for single recipe_equipment"""
        try:
            recipe_equipment = RecipeEquipment.objects.get(pk=pk)
            serializer = RecipeEquipmentSerializer(recipe_equipment)

            return Response(serializer.data)

        except RecipeEquipment.DoesNotExist as ex:

            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handles GET requests to get all recipe_equipment"""
        recipe_equipment = RecipeEquipment.objects.all()
        serializer = RecipeEquipmentSerializer(recipe_equipment, many=True)
        recipe = request.query_params.get('recipeId')
        try:
            if recipe is not None:
                equip_by_recipe = recipe_equipment.filter(recipe_id=recipe)
                serializer = RecipeEquipmentSerializer(equip_by_recipe, many=True)

                return Response(serializer.data)

        except RecipeEquipment.DoesNotExist as ex:

            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data)

class RecipeEquipmentSerializer(serializers.ModelSerializer):
    """Serilizer for Method Class"""
    class Meta:
        model = RecipeEquipment
        fields = (
          'id',
          'type',
          'name',
          'recipe_id',
          'setting',
        )
