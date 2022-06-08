import base64
import json
import logging

from django.contrib.auth import authenticate, login, logout
from django.core.files.base import ContentFile
from django.http import JsonResponse
from rest_framework.authtoken.models import Token

from user.models import CustomUser
from user.serializers import UserSerializer

logger = logging.getLogger(__name__)


def auth(request):
    data = json.loads(request.body.decode('utf8').replace("'", '"'))
    user = authenticate(username=data['email'], password=data['password'])

    if user is not None:
        login(request, user)
        user_token = Token.objects.filter(user=user.id)
        if user_token:
            user_token.delete()

        Token.objects.create(user=user)

        serializer = UserSerializer(user)

        return JsonResponse(serializer.data)
    else:
        logger.error('Something went wrong in login!')
        raise Exception('Error in login')


def update_user(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf8').replace("'", '"'))
        user = CustomUser.objects.get(pk=data['user_id'])

        if request.user != user:
            logger.error(f'User {request.user.username} trying modify another '
                         f'user')
            raise Exception('You cannot modify this user')

        update_fields = ['name', 'email', 'first_name', 'last_name']
        user.name = data.get("name", user.name)
        user.email = data.get("email", user.email)
        user.first_name = data.get("first_name", user.first_name)
        user.last_name = data.get("last_name", user.last_name)
        if data.get("avatar"):
            format, imgstr = data.get("avatar").split(';base64,')
            ext = format.split('/')[-1]

            img = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
            update_fields.append('avatar')
            user.avatar = img

        if data.get("password"):
            update_fields.append('password')
            user.set_password(data.get('password'))

        user.save(update_fields=update_fields)

        if data.get("password"):
            user = authenticate(username=data['email'],
                                password=data['password'])
            login(request, user)
            user_token = Token.objects.filter(user=user.id)

            if user_token:
                user_token.delete()

            Token.objects.create(user=user)

        serializer = UserSerializer(user)

        return JsonResponse(serializer.data)


def user_logout(request):
    request.user.auth_token.delete()
    logout(request)

    return JsonResponse({'message': 'ok'})
