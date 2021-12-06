from rest_framework import serializers
from rest_framework.authtoken.models import Token

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'token',
            'id',
        ]

    def get_token(self, obj):
        token, created = Token.objects.get_or_create(user=obj)
        return token.key
