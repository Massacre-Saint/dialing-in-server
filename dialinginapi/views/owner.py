"""Module for all methods"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers,status
from dialinginapi.models import Owner, User

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
        """Handles GET request for all favorites"""
        owner_recipes = Owner.objects.all()

        try:
            uid = request.META['HTTP_AUTHORIZATION']
            user = User.objects.get(uid=uid)
            try:
                user_recipes = owner_recipes.filter(user_id = user.id)
                serializer = OwnerSerializer(user_recipes, many=True)
                return Response(serializer.data)
            except Owner.DoesNotExist as ex:

                return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except User.DoesNotExist as ex:

            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

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
