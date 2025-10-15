import pytest
from apps.users.models import User
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


@pytest.mark.django_db
def test_token_serializer_debug():
    User.objects.filter(username='dbg_user').delete()
    User.objects.create_user('dbg_user', 'dbg@example.com', 'dbgpass')
    s = TokenObtainPairSerializer(data={'username': 'dbg_user', 'password': 'dbgpass'})
    # additional checks
    u = User.objects.filter(username='dbg_user').first()
    assert u is not None
    auth_user = authenticate(username='dbg_user', password='dbgpass')
    if auth_user is None:
        # include check_password result for debugging
        pwd_ok = u.check_password('dbgpass')
        pytest.fail(
            f"authenticate returned None; user.check_password -> {pwd_ok}; is_active -> {u.is_active}; pk -> {u.pk}; username -> {u.username}; "
            f"AUTH_USER_MODEL={settings.AUTH_USER_MODEL}; user_model_module={get_user_model().__module__}; "
            f"AUTHENTICATION_BACKENDS={getattr(settings, 'AUTHENTICATION_BACKENDS', None)}"
        )
    try:
        valid = s.is_valid()
    except Exception as e:
        # make the exception visible in pytest output
        pytest.fail(f"Serializer raised exception: {type(e).__name__}: {e}")
    # If not valid, fail with serializer errors printed
    if not valid:
        pytest.fail(f"Serializer not valid, errors: {s.errors}")
