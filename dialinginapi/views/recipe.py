"""Module for all methods"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from dialinginapi.models import Recipe, Method, Grind

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
    
    def create(self, request):
        """_summary_

        Args:
            request (_type_): _description_
        """
        payload = request.data
        if payload:
            method = Method.objects.get(pk = request.data['method_id'])
            if method:
                recipe = Recipe.objects.create (
                    default = False,
                    method_id = method,
                    published = False
                )
            serializer = RecipeSerializer(recipe)

        recipe = Recipe.objects.create (
            default = False,
            published = False,
            
        )
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """_summary_

        Args:
            request (_type_): _description_
            pk (_type_): _description_
        """
        body = request.data
        recipe = Recipe.objects.get(pk = pk)
        if 'method_id' in body:
            method = Method.objects.get(pk=body['method_id'])
            recipe.method_id = method
        else:
            recipe.method_id = None
        if 'grind_id' in body:
            grind = Grind.objects.get(pk=body['grind_id'])
            recipe.grind_id = grind
        else:
            recipe.grind_id = None
        if 'weight' in body:
            recipe.weight = request.data['weight']
        else:
            recipe.weight = None
        if 'dose' in body:
            recipe.dose = request.data['dose']
        else:
            recipe.dose = None
        if 'brew_time' in body:
            recipe.brew_time = request.data['brew_time']
        else:
            recipe.brew_time = None
        if 'published' in body:
            recipe.published = request.data['published']
        else:
            recipe.published = None
        if 'recipe_name' in body:
            recipe.recipe_name = request.data['recipe_name']
        else:
            recipe.recipe_name = None

        recipe.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """_summary_

        Args:
            request (_type_): _description_
            pk (_type_): _description_

        Returns:
            _type_: _description_
        """
        recipe = Recipe.objects.get(pk = pk)
        recipe.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
class RecipeSerializer(serializers.ModelSerializer):
    """Serilizer for User Class"""
    class Meta:
        depth = 2
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
