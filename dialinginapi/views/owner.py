"""Module for all methods"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers,status
from dialinginapi.models import Owner, User, Recipe, Method

class OwnerView(ViewSet):
    """Class creates viewset for Favorite"""
    def retrieve(self, request, pk):
        """Handles GET request for single Favorite """
        try:
            owner = Owner.objects.get(pk=pk)
            serializer = OwnerSerializer(owner)

            return Response(serializer.data)

        except Owner.DoesNotExist as ex:

            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
  
    def list(self, request):
        """Handles GET requests for Owner Class"""
        # Decide if auth header is present
        owner_recipes = Owner.objects.all()
        user_id = request.query_params.get('userId', None)
        method_id = request.query_params.get('methodId', None)

        try:
            if user_id is not None:
                recipes_by_user_id = owner_recipes.filter(user_id = user_id)
                serializer = OwnerSerializer(recipes_by_user_id, many=True)

                return Response(serializer.data)
        except Recipe.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        if 'Authorization' in request.headers:
            uid = request.META['HTTP_AUTHORIZATION']

            try:
                user = User.objects.get(uid=uid)
                your_recipes = owner_recipes.filter(user_id = user.id)
                serializer = OwnerSerializer(your_recipes, many=True)

                return Response(serializer.data)

            except User.DoesNotExist as ex:
            # Error handling for user not existing
                return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        try:
            if method_id is not None:
                recipes = Recipe.objects.all()
                user_recipes_by_method = recipes.filter(method_id = method_id, default = False, published = True)
                final = owner_recipes.filter(recipe_id__id=user_recipes_by_method.method_id)
                serializer = OwnerSerializer(final, many=True)

                return Response(serializer.data)

        except Owner.DoesNotExist as ex:
            # Error handling for no owner recipes
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        serializer= OwnerSerializer(owner_recipes, many=True)
        return Response(serializer.data)
class OwnerSerializer(serializers.ModelSerializer):
    """Serilizer for Owner Class"""
    class Meta:
        depth = 1
        model = Owner
        fields = (
        #     'id',
        #   'brew_time',
        #   'grind_id',
        #   'weight',
        #   'dose',
        #   'method_id',
        #   'recipe_name',
        #   'default',
        #   'published',
          'id',
          'user_id',
          'recipe_id',
        )
