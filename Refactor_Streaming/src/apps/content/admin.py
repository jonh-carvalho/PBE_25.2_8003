"""
Content admin configuration.
"""
from django.contrib import admin
from .models import Content


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    """Admin interface for Content model."""
    
    list_display = ['title', 'creator', 'content_type', 'status', 'is_public', 'views_count', 'created_at']
    list_filter = ['content_type', 'status', 'is_public', 'created_at']
    search_fields = ['title', 'description', 'creator__username']
    readonly_fields = ['views_count', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('title', 'description', 'creator')
        }),
        ('Arquivo', {
            'fields': ('file_url', 'thumbnail_url', 'content_type', 'duration', 'file_size')
        }),
        ('Configurações', {
            'fields': ('status', 'is_public')
        }),
        ('Estatísticas', {
            'fields': ('views_count', 'likes_count'),
            'classes': ('collapse',)
        }),
        ('Datas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )