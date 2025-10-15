"""
Content serializers for the streaming platform.
"""
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()
from .models import Content, ContentStatus, ContentType


class ContentCreatorSerializer(serializers.ModelSerializer):
    """Serializer for content creator information."""
    
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class ContentSerializer(serializers.ModelSerializer):
    """Serializer for content."""
    
    creator = ContentCreatorSerializer(read_only=True)
    
    class Meta:
        model = Content
        fields = [
            'id',
            'title',
            'description',
            'file_url',
            'thumbnail_url',
            'content_type',
            'duration',
            'is_public',
            'status',
            'creator',
            'views_count',
            'likes_count',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'views_count', 'likes_count', 'created_at', 'updated_at', 'creator']