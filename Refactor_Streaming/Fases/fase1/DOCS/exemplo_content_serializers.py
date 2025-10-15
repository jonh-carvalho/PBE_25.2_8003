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


class ContentListSerializer(serializers.ModelSerializer):
    """Serializer for content list view."""
    
    creator = ContentCreatorSerializer(read_only=True)
    file_url = serializers.URLField(read_only=True)
    
    class Meta:
        model = Content
        fields = [
            'id',
            'title',
            'description',
            'file_url',
            'thumbnail',
            'content_type',
            'duration',
            'is_public',
            'status',
            'creator',
            'views_count',
            'likes_count',
            'created_at',
        ]
        read_only_fields = ['id', 'views_count', 'likes_count', 'created_at']


class ContentDetailSerializer(serializers.ModelSerializer):
    """Serializer for content detail view."""
    
    creator = ContentCreatorSerializer(read_only=True)
    file_url = serializers.URLField(read_only=True)
    
    class Meta:
        model = Content
        fields = [
            'id',
            'title',
            'description',
            'file',
            'file_url',
            'thumbnail',
            'content_type',
            'duration',
            'file_size',
            'is_public',
            'status',
            'creator',
            'views_count',
            'likes_count',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'file_url',
            'file_size',
            'creator',
            'views_count',
            'likes_count',
            'created_at',
            'updated_at',
        ]


class ContentCreateSerializer(serializers.ModelSerializer):
    """Serializer for content creation."""
    
    class Meta:
        model = Content
        fields = [
            'title',
            'description',
            'file',
            'thumbnail',
            'content_type',
            'is_public',
            'status',
        ]
    
    def validate_file(self, value):
        """Validate uploaded file."""
        if not value:
            raise serializers.ValidationError("Arquivo é obrigatório.")
        
        # Check file size (max 100MB)
        max_size = 100 * 1024 * 1024  # 100MB
        if value.size > max_size:
            raise serializers.ValidationError(
                "Arquivo muito grande. Tamanho máximo permitido: 100MB."
            )
        
        return value
    
    def validate_content_type(self, value):
        """Validate content type based on file extension."""
        if 'file' in self.initial_data:
            file = self.initial_data['file']
            if hasattr(file, 'name'):
                file_name = file.name.lower()
                
                video_extensions = ['.mp4', '.avi', '.mov', '.mkv']
                audio_extensions = ['.mp3', '.wav', '.flac', '.aac']
                
                if value == ContentType.VIDEO:
                    if not any(file_name.endswith(ext) for ext in video_extensions):
                        raise serializers.ValidationError(
                            "Arquivo deve ser um vídeo válido (.mp4, .avi, .mov, .mkv)."
                        )
                
                elif value == ContentType.AUDIO:
                    if not any(file_name.endswith(ext) for ext in audio_extensions):
                        raise serializers.ValidationError(
                            "Arquivo deve ser um áudio válido (.mp3, .wav, .flac, .aac)."
                        )
        
        return value


class ContentUpdateSerializer(serializers.ModelSerializer):
    """Serializer for content updates."""
    
    class Meta:
        model = Content
        fields = [
            'title',
            'description',
            'thumbnail',
            'is_public',
            'status',
        ]
    
    def validate_status(self, value):
        """Validate status transitions."""
        if self.instance:
            current_status = self.instance.status
            
            # Define allowed transitions
            allowed_transitions = {
                ContentStatus.DRAFT: [ContentStatus.PUBLISHED, ContentStatus.ARCHIVED],
                ContentStatus.PUBLISHED: [ContentStatus.ARCHIVED],
                ContentStatus.ARCHIVED: [ContentStatus.PUBLISHED],
            }
            
            if value not in allowed_transitions.get(current_status, []):
                raise serializers.ValidationError(
                    f"Transição de status inválida: {current_status} -> {value}"
                )
        
        return value