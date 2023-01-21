"""Module for all methods"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers,status
from dialinginapi.models import Owner, User, Recipe

class OwnerView(ViewSet):
    """Class creates viewset for Favorite"""
    def retrieve(self, request, pk):
        """Handles GET request for single Favorite """
        try:
            owner = Owner.objects.get(recipe_id=pk)
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

                # return Response(serializer.data)
        except Recipe.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        if 'Authorization' in request.headers:
            uid = request.META['HTTP_AUTHORIZATION']

            try:
                user = User.objects.get(uid=uid)
                your_recipes = owner_recipes.filter(user_id = user.id)
                serializer = OwnerSerializer(your_recipes, many=True)
                # return Response(serializer.data)

            except User.DoesNotExist as ex:
            # Error handling for user not existing
                return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        try:
            if method_id is not None:
                print('methodId')
                # recipes = Recipe.objects.all()
                # user_recipes_by_method = recipes.filter(method_id = method_id, default = False, published = True)
                # final = owner_recipes.filter(recipe_id__id = user_recipes_by_method[0].pk)
                # serializer = OwnerSerializer(final, many=True)

                # return Response(serializer.data)
                recipes = Recipe.objects.all()
                user_recipes_by_method = recipes.filter(method_id = method_id, default = False, published = True)
                final = []
                print(len(user_recipes_by_method))
                if len(user_recipes_by_method) > 0:
                    for recipe in user_recipes_by_method:
                        rid = recipe.id
                        for owner in owner_recipes:
                            oid = owner.recipe_id_id
                            if oid == rid:
                                final.append(owner)
                                
                        serializer = OwnerSerializer(final, many=True)
                        owner_serialized = serializer.data
                        for i in owner_serialized:
                            final.append(i)
                            return Response(owner_serialized)
                else:
                    return Response([])
                
                
        except Owner.DoesNotExist as ex:
            # Error handling for no owner recipes
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        print('last return')
        serializer= OwnerSerializer(owner_recipes, many=True)
        return Response(serializer.data)
class OwnerSerializer(serializers.ModelSerializer):
    """Serilizer for Owner Class"""
    class Meta:
        depth = 2
        model = Owner
        fields = (
          'id',
          'user_id',
          'recipe_id',
        )
