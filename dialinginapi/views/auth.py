"""Module handles user"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dialinginapi.models import User

@api_view(['POST'])
def check_user(request):
    """Check to see if user has associated User Class

    Args:
        request: The full HTTP request object
    """

    uid = request.data['uid']

    try:
        user = User.objects.get(uid=uid)
        data = {
          'id': user.id,
          'uid': user.uid,
          'image_url': user.image_url,
          'name': user.name,
        }
        return Response(data)

    except: # pylint: disable=bare-except
      # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)

@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    user = User.objects.create(
      uid = request.data['uid'],
      image_url = request.data['image_url'],
      name = request.data['name'],
    )
    data = {
      'id': user.id,
      'uid': user.uid,
      'image_url': user.image_url,
      'name': user.name
    }
    return Response(data)
