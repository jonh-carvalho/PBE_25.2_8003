"""
Tests for Content model and API.
"""
import pytest
from django.contrib.auth.models import User
from apps.content.models import Content


@pytest.mark.django_db
class TestContentModel:
    """Test Content model."""
    
    def test_content_creation(self, user):
        """Test content creation."""
        content = Content.objects.create(
            title='Test Video',
            description='Test description',
            file_url='https://example.com/video.mp4',
            content_type='video',
            creator=user
        )
        assert content.title == 'Test Video'
        assert content.creator == user
        assert content.status == 'draft'  # default status
        assert content.is_public is True  # default is public
    
    def test_content_str_representation(self, user):
        """Test content string representation."""
        content = Content.objects.create(
            title='Test Video',
            creator=user
        )
        assert str(content) == 'Test Video'


@pytest.mark.django_db
class TestContentAPI:
    """Test Content API endpoints."""
    
    def test_content_list_unauthenticated(self, api_client):
        """Test content list for unauthenticated user."""
        response = api_client.get('/api/content/')
        # Should return public content, not 401
        assert response.status_code == 200
    
    def test_content_list_authenticated(self, authenticated_client, user, content_data):
        """Test content list for authenticated user."""
        # Create content
        Content.objects.create(**content_data, creator=user)
        
        response = authenticated_client.get('/api/content/')
        assert response.status_code == 200
        assert len(response.data['results']) >= 1
    
    def test_content_create(self, authenticated_client, content_data):
        """Test content creation via API."""
        response = authenticated_client.post('/api/content/', content_data)
        assert response.status_code == 201
        assert response.data['title'] == content_data['title']
    
    def test_content_retrieve(self, authenticated_client, user, content_data):
        """Test content detail retrieval."""
        content = Content.objects.create(**content_data, creator=user)
        
        response = authenticated_client.get(f'/api/content/{content.id}/')
        assert response.status_code == 200
        assert response.data['title'] == content.title