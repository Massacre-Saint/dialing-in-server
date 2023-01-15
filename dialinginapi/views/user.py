"""Module for all methods"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from dialinginapi.models import User

class UserView(ViewSet):
    """Class create viewset for User"""
    def retrieve(self, request, pk):
        """Get single user method"""
        uid = request.META['HTTP_AUTHORIZATION']

        user = User.objects.get(uid=uid)
        serializer = UserSerializer(user)

        return Response(serializer.data)
class UserSerializer(serializers.ModelSerializer):
    """Serilizer for User Class"""
    class Meta:
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
