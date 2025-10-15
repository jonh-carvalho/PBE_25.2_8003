"""
Content views for the streaming platform.
"""
from django.db import models
from rest_framework import viewsets, permissions
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import Content
from .serializers import ContentSerializer


@extend_schema_view(
    list=extend_schema(
        description="Lista todos os conteúdos públicos",
        tags=["Content"]
    ),
    create=extend_schema(
        description="Cria um novo conteúdo (requer autenticação)",
        tags=["Content"]
    ),
    retrieve=extend_schema(
        description="Obtém detalhes de um conteúdo específico",
        tags=["Content"]
    ),
    update=extend_schema(
        description="Atualiza um conteúdo existente (apenas o criador)",
        tags=["Content"]
    ),
    destroy=extend_schema(
        description="Remove um conteúdo (apenas o criador)",
        tags=["Content"]
    ),
)
class ContentViewSet(viewsets.ModelViewSet):
    """ViewSet for Content management."""
    
    queryset = Content.objects.filter(is_public=True, status='published')
    serializer_class = ContentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Set the creator to the current user."""
        serializer.save(creator=self.request.user)
    
    def get_queryset(self):
        """Filter queryset based on user permissions."""
        queryset = Content.objects.all()
        
        if self.request.user.is_authenticated:
            # Authenticated users can see their own content
            return queryset.filter(
                models.Q(is_public=True, status='published') |
                models.Q(creator=self.request.user)
            )
        else:
            # Anonymous users only see public published content
            return queryset.filter(is_public=True, status='published')