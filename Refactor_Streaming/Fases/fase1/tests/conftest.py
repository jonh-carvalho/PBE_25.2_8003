"""
Pytest configuration and fixtures.
"""
import os
import django
from django.conf import settings

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
django.setup()

import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    """Return API client for testing."""
    return APIClient()


@pytest.fixture
def user():
    """Create a test user."""
    return User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='testpass123'
    )


@pytest.fixture
def authenticated_client(api_client, user):
    """Return authenticated API client."""
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def content_data():
    """Return sample content data."""
    return {
        'title': 'Test Content',
        'description': 'Test description',
        'file_url': 'https://example.com/test.mp4',
        'content_type': 'video',
        'is_public': True,
        'status': 'published'
    }