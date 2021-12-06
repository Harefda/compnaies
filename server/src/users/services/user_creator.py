from users.models import User
from app.errors import ObjectAlreadyExists
from users.utils import UserErrorMessages


class UserCreator:
    def __init__(self, email, password):
        self.email = email
        self.password = password
    
    def __call__(self):
        pass

    def create_user(self):
        return User.objects.create(
            email=self.email,
            password=self.password
        )

    def allowed_to_create(self, raise_exception=True):
        try:
            if User.objects.filter(email=self.email).exists():
                raise ObjectAlreadyExists
            if len(self.password) <= 3:
                raise UserErrorMessages(UserErrorMessages.INCORRECT_PASSWORD_SCHEME_ERROR.value)
        except ObjectAlreadyExists as exc:
            if raise_exception:
                raise exc
            else:
                return False

        return True