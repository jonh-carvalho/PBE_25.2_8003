"""Tests for custom User model."""
import pytest
from apps.users.models import User


@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
    assert user.username == 'testuser'
    assert user.email == 'test@example.com'
    assert user.check_password('testpass')
    assert user.is_verified is False
