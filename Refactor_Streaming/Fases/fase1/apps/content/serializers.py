"""
Content serializers for the streaming platform.
"""
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Content, ContentType, ContentStatus


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