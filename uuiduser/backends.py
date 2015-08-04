from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.auth.backends import ModelBackend


PRIMARY_EMAIL_LOGIN_ONLY = getattr(settings,
                                   'UUIDUSER_PRIMARY_EMAIL_LOGIN_ONLY',
                                   True)


class UUIDUserBackend(ModelBackend):
  """Authenticates against settings.AUTH_USER_MODEL."""

  def authenticate(self, username=None, password=None, **kwargs):
    UserModel = get_user_model()

    if username is None:
      username = kwargs.get(UserModel.USERNAME_FIELD)

    try:
      user = UserModel.objects.username(username)
    except UserModel.DoesNotExist:
      try:
        if PRIMARY_EMAIL_LOGIN_ONLY:
          user = UserModel.get_by_email(username, primary_only=True)
        else:
          user = UserModel.get_by_email(username, primary_only=False)
      except UserModel.DoesNotExist:
        # Run the default password hasher once to reduce the timing
        # difference between an existing and a non-existing user (#20760).
        UserModel().set_password(password)
        return None

    if user.check_password(password):
      return user
