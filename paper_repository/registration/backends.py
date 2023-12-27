from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend, UserModel

from .models import CustomUser


class CaseInsensitiveModelBackend(ModelBackend):
    """
    This is a ModelBacked that allows authentication with a case insensitive
    username.
    """

    def authenticate(self, request=None, password=None, **kwargs):
        user = CustomUser
        email = kwargs.get('username', None)
        if email is None:
            email = kwargs.get(user.USERNAME_FIELD)
        case_insensitive_username_field = '{}__iexact'.format(user.USERNAME_FIELD)
        user = user.objects.get(email = email)
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
