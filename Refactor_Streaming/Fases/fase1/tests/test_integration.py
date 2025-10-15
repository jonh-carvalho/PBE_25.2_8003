"""
Integration tests for the streaming platform.
"""
import pytest
from django.contrib.auth.models import User
from apps.content.models import Content


@pytest.mark.integration
@pytest.mark.django_db
class TestContentWorkflow:
    """Test complete content workflow."""
    
    def test_complete_content_lifecycle(self, authenticated_client, content_data):
        """Test complete content lifecycle: create, update, publish, delete."""
        # Create content
        response = authenticated_client.post('/api/content/', content_data)
        assert response.status_code == 201
        content_id = response.data['id']
        
        # Update content
        update_data = {'title': 'Updated Title', 'status': 'published'}
        response = authenticated_client.patch(f'/api/content/{content_id}/', update_data)
        assert response.status_code == 200
        assert response.data['title'] == 'Updated Title'
        assert response.data['status'] == 'published'
        
        # Retrieve updated content
        response = authenticated_client.get(f'/api/content/{content_id}/')
        assert response.status_code == 200
        assert response.data['title'] == 'Updated Title'
        
        # Delete content
        response = authenticated_client.delete(f'/api/content/{content_id}/')
        assert response.status_code == 204
        
        # Verify deletion
        response = authenticated_client.get(f'/api/content/{content_id}/')
        assert response.status_code == 404