"""Module for all methods"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from dialinginapi.models import Recipe

class RecipeView(ViewSet):
    """Class creates viewset for Recipe"""
    def retrieve(self, request, pk):
        """Get single receipe method"""
        try:
            recipe = Recipe.objects.get(pk=pk)
            serializer = RecipeSerializer(recipe)

            return Response(serializer.data)

        except Recipe.DoesNotExist as ex:

            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """_summary_

        Args:
            request (_get_): Availible query_params are
              methodId = __

        Returns:
            Response: All recipes or queried recipes by methodId
        """
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        method = request.query_params.get('methodId', None)
        default = request.query_params.get('default',None)

        if default is not None:
            recipes_by_default = recipes.filter(default = True)
            method_recipes_by_default = recipes_by_default.filter(method_id =method)
            serializer= RecipeSerializer(method_recipes_by_default, many= True)
            return Response(serializer.data)
        try:
            if method is not None:
                recipes_by_method = recipes.filter(method_id = method)
                serializer = RecipeSerializer(recipes_by_method, many=True)
                return Response(serializer.data)

        except Recipe.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data)
class RecipeSerializer(serializers.ModelSerializer):
    """Serilizer for User Class"""
    class Meta:
        depth = 1
        model = Recipe
        fields = (
          'id',
          'brew_time',
          'grind_id',
          'weight',
          'dose',
          'method_id',
          'recipe_name',
          'default',
          'published',
          )
