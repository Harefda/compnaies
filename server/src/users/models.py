from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
)


class UserManager(BaseUserManager):
    def create_user(self, email, password, is_active=True, is_admin=False, is_staff=False):
        if not password:
            raise ValueError("User must have a password")
        if not email:
            raise ValueError("User must have an email")

        email = email.lower()

        user = self.model(
            email=email,
        )
        user.set_password(password)
        user.is_active = is_active
        user.is_staff = is_staff
        user.is_admin = is_admin
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=email,
            password=password,
            is_admin=True,
            is_staff=True
        )
        print(user)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    objects = UserManager()
    class Meta:
        verbose_name = ("User")
        verbose_name_plural = ("Users")

    @property
    def is_company(self):
        try:
            return self.company is not None
        except AttributeError:
            return False

    @property
    def is_department(self):
        try:
            return self.employee is not None
        except AttributeError:
            return False

    def __str__(self):
        return f'<User {self.email}>'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True