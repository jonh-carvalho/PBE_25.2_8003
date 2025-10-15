"""Integration tests for JWT authentication."""
import pytest
from apps.users.models import User
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestAuth:
    def test_login_refresh_logout(self):
        client = APIClient()
        # create user
        User.objects.create_user(username='authuser', email='auth@example.com', password='authpass')

        # login
        resp = client.post('/api/auth/login/', {'username': 'authuser', 'password': 'authpass'}, format='json')
        assert resp.status_code == 200
        assert 'access' in resp.data
        assert 'refresh' in resp.data

        refresh = resp.data['refresh']

        # refresh
        resp2 = client.post('/api/auth/refresh/', {'refresh': refresh}, format='json')
        assert resp2.status_code == 200
        assert 'access' in resp2.data

        # logout (requires authentication)
        access = resp2.data['access']
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access}')
        resp3 = client.post('/api/auth/logout/', {'refresh': refresh}, format='json')
        assert resp3.status_code in (204, 200)
