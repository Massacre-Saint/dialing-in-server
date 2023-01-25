"""Module for all methods"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from dialinginapi.models import User, Method

class UserView(ViewSet):
    """Class create viewset for User"""
    def retrieve(self, request,pk):
        """Get single user method"""

        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)

            return Response(serializer.data)
        except User.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request,pk):
        """Method handles PUT request for updating user"""
        user = User.objects.get(pk=pk)
        method_id = Method.objects.get(pk=request.data['methodId'])

        user.method_id = method_id
        user.fav_roast = request.data['favRoast']
        user.fav_shop = request.data['favShop']
        user.description = request.data['description']
        user.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
class UserSerializer(serializers.ModelSerializer):
    """Serilizer for User Class"""
    class Meta:
        depth = 1
        model = User
        fields = (
          'id',
          'uid',
          'name',
          'method_id',
          'fav_roast',
          'fav_shop',
          'description',
          'image_url',
          )
