"""Module for all methods"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers,status
from dialinginapi.models import Favorite, User, Recipe
class FavoriteView(ViewSet):
    """Class creates viewset for Favorite"""
    def retrieve(self, request, pk):
        """Handles GET request for single Favorite """
        try:
            favorites= Favorite.objects.all()
            favorite = favorites.get(pk=pk)
            serializer = FavoriteSerializer(favorite)

            return Response(serializer.data)

        except Favorite.DoesNotExist as ex:

            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Handles GET requests for all favorites"""
        favorites = Favorite.objects.all()
        recipe_id = request.query_params.get('recipeId', None)
        uid = request.META['HTTP_AUTHORIZATION']
        
        try:
            user = User.objects.get(uid=uid)
            favorites_by_user = favorites.filter(user_id_id = user.id)
            
            if len(favorites_by_user) > 0:
                if recipe_id is not None:
                    favorite_recipe = favorites_by_user.filter(recipe_id_id = recipe_id)
                    if len(favorite_recipe) > 0:
                        serializer = FavoriteSerializer(favorite_recipe, many=True)
                        return Response(serializer.data)
                    else:
                        return Response({})
            else:
                return Response([])

        except User.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        serializer = FavoriteSerializer(favorites_by_user, many=True)
        return Response(serializer.data)

    def create(self, request):
        """_summary_

        Args:
            request (_type_): _description_
        """
        recipe = Recipe.objects.get(pk = request.data['recipe_id'])
        uid = request.META['HTTP_AUTHORIZATION']
        user = User.objects.get(uid=uid)

        favorite = Favorite.objects.create(
            user_id = user,
            recipe_id = recipe,
        )
        serializer = FavoriteSerializer(favorite)
        return Response(serializer.data)
    
    def destroy(self, request, pk):
        """_summary_

        Args:
            rquest (_type_): _description_
            pk (_type_): _description_
        """
        favorite = Favorite.objects.get(pk=pk)
        favorite.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
class FavoriteSerializer(serializers.ModelSerializer):
    """Serilizer for Favorite Class"""
    class Meta:
        depth = 2
        model = Favorite
        fields = (
          'id',
          'user_id',
          'recipe_id',
        )
