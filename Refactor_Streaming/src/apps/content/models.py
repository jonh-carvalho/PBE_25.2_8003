"""
Content models for the streaming platform.
"""
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from apps.common.models import TimeStampedModel


class ContentType(models.TextChoices):
    AUDIO = 'audio', 'Áudio'
    VIDEO = 'video', 'Vídeo'


class ContentStatus(models.TextChoices):
    DRAFT = 'draft', 'Rascunho'
    PUBLISHED = 'published', 'Publicado'
    ARCHIVED = 'archived', 'Arquivado'


class Content(TimeStampedModel):
    """Model for audio and video content."""
    
    title = models.CharField(
        max_length=255,
        verbose_name='Título'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Descrição'
    )
    
    # File handling
    file_url = models.URLField(
        verbose_name='URL do Arquivo'
    )
    thumbnail_url = models.URLField(
        blank=True,
        null=True,
        verbose_name='URL da Miniatura'
    )
    
    # Content metadata
    content_type = models.CharField(
        max_length=10,
        choices=ContentType.choices,
        verbose_name='Tipo de Conteúdo'
    )
    duration = models.DurationField(
        blank=True,
        null=True,
        verbose_name='Duração'
    )
    file_size = models.BigIntegerField(
        blank=True,
        null=True,
        verbose_name='Tamanho do Arquivo (bytes)'
    )
    
    # Content settings
    is_public = models.BooleanField(
        default=True,
        verbose_name='Público'
    )
    status = models.CharField(
        max_length=20,
        choices=ContentStatus.choices,
        default=ContentStatus.DRAFT,
        verbose_name='Status'
    )
    
    # Relationships
    creator = models.ForeignKey(
        User,
        related_name='contents',
        on_delete=models.CASCADE,
        verbose_name='Criador'
    )
    
    # Statistics
    views_count = models.PositiveIntegerField(
        default=0,
        verbose_name='Visualizações'
    )
    likes_count = models.PositiveIntegerField(
        default=0,
        verbose_name='Curtidas'
    )
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Conteúdo'
        verbose_name_plural = 'Conteúdos'
        indexes = [
            models.Index(fields=['status', 'is_public']),
            models.Index(fields=['content_type']),
            models.Index(fields=['creator']),
        ]
    
    def __str__(self):
        return self.title
    
    def increment_views(self):
        """Increment views count."""
        self.views_count += 1
        self.save(update_fields=['views_count'])