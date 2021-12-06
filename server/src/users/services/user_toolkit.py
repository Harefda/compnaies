from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from users.models import User
from users.utils import UserErrorMessages
from app.errors import ValidationError


class UserToolKit:
    @classmethod
    def create_user(cls, email, password):
        from users.services import UserCreator
        user = UserCreator(
            email=email,
            password=password
        )()
        return user

    @classmethod
    def authenticate_user(cls, email, password):
        user = authenticate(email=email, password=password)
        if not user:
            qs = User.objects.filter(email=email)
            if qs.exists() and not qs.first().is_active:
                raise ValidationError(UserErrorMessages.DISABLED_USER_ERROR.value)
            raise ValidationError(UserErrorMessages.CREDENTIALS_ERROR.value)

        return user, Token.objects.get_or_create(user=user)[0]