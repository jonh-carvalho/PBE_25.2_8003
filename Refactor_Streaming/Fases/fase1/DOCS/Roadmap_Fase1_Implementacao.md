# 🚀 Implementação Roadmap Fase 1 - Django REST API Streaming

## 📋 **Objetivo da Fase 1**

Modernizar e reestruturar o projeto Django REST API Streaming com foco em:
- Atualizar dependências desatualizadas 
- Implementar estrutura multi-app
- Adicionar testes básicos
- Configurar Docker para desenvolvimento

## 🔧 **1. Atualização de Dependências**

### 1.1 Novo arquivo `requirements/base.txt`

```txt
# Django Core
Django>=4.2.0,<5.0
djangorestframework>=3.14.0

# API Documentation (Moderno - substitui drf-yasg)
drf-spectacular>=0.26.0

# CORS Support
django-cors-headers>=4.0.0

# Environment Variables
python-decouple>=3.8
python-dotenv>=1.0.0

# Database
psycopg2-binary>=2.9.0  # PostgreSQL

# Media/File Handling
Pillow>=10.0.0

# Utilities
django-extensions>=3.2.0
```

### 1.2 Arquivo `requirements/development.txt`

```txt
-r base.txt

# Development Tools
django-debug-toolbar>=4.1.0
ipython>=8.12.0

# Testing
pytest>=7.4.0
pytest-django>=4.5.0
pytest-cov>=4.1.0
factory-boy>=3.2.0

# Code Quality
black>=23.0.0
isort>=5.12.0
flake8>=6.0.0
mypy>=1.4.0
django-stubs>=4.2.0

# Pre-commit hooks
pre-commit>=3.3.0
```

### 1.3 Arquivo `requirements/production.txt`

```txt
-r base.txt

# Production Server
gunicorn>=21.0.0

# Cache
redis>=4.6.0
django-redis>=5.3.0

# Monitoring
sentry-sdk>=1.28.0

# Security
django-ratelimit>=4.0.0
```

## 🏗️ **2. Nova Estrutura Multi-App**

### 2.1 Estrutura de Diretórios

```
streaming_platform/
├── config/
│   ├── __init__.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── development.py
│   │   ├── production.py
│   │   └── testing.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apps/
│   ├── __init__.py
│   ├── authentication/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── tests/
│   ├── content/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   └── tests/
│   ├── playlists/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── tests/
│   ├── users/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── tests/
│   └── common/
│       ├── __init__.py
│       ├── permissions.py
│       ├── pagination.py
│       ├── mixins.py
│       └── utils.py
├── requirements/
│   ├── base.txt
│   ├── development.txt
│   └── production.txt
├── docker/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── entrypoint.sh
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── integration/
├── static/
├── media/
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── manage.py
├── pytest.ini
└── README.md
```

## ⚙️ **3. Configurações Modernas**

### 3.1 Arquivo `config/settings/base.py`

```python
"""
Base settings for streaming_platform project.
"""
import os
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='your-secret-key-here')

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'drf_spectacular',
    'corsheaders',
]

LOCAL_APPS = [
    'apps.authentication',
    'apps.content',
    'apps.playlists',
    'apps.users',
    'apps.common',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='streaming_db'),
        'USER': config('DB_USER', default='streaming_user'),
        'PASSWORD': config('DB_PASSWORD', default='streaming_pass'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS': 'apps.common.pagination.StandardResultsSetPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}

# DRF Spectacular (API Documentation)
SPECTACULAR_SETTINGS = {
    'TITLE': 'Streaming Platform API',
    'DESCRIPTION': 'API para plataforma de streaming de áudio e vídeo',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST': True,
    'SORT_OPERATIONS': False,
}

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # React development
    "http://127.0.0.1:3000",
    "http://localhost:8080",  # Vue development
    "http://127.0.0.1:8080",
]

CORS_ALLOW_CREDENTIALS = True
```

### 3.2 Arquivo `config/settings/development.py`

```python
"""
Development settings for streaming_platform project.
"""
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

# Development-specific apps
INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]

# Debug Toolbar
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]

# Email backend for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# CORS settings for development
CORS_ALLOW_ALL_ORIGINS = True
```

### 3.3 Arquivo `config/settings/production.py`

```python
"""
Production settings for streaming_platform project.
"""
from .base import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

DEBUG = False

ALLOWED_HOSTS = [
    config('ALLOWED_HOST', default='your-domain.com'),
]

# Security settings
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# Sentry configuration
sentry_sdk.init(
    dsn=config('SENTRY_DSN', default=''),
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True
)

# Cache configuration
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': config('REDIS_URL', default='redis://127.0.0.1:6379/1'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# Rate limiting
RATELIMIT_ENABLE = True
```

## 📝 **4. Modelos Refatorados**

### 4.1 Arquivo `apps/content/models.py`

```python
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
    file = models.FileField(
        upload_to='content/%Y/%m/',
        validators=[
            FileExtensionValidator(
                allowed_extensions=['mp4', 'mp3', 'avi', 'wav', 'mov']
            )
        ],
        verbose_name='Arquivo'
    )
    thumbnail = models.ImageField(
        upload_to='thumbnails/%Y/%m/',
        blank=True,
        null=True,
        verbose_name='Miniatura'
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
    
    @property
    def file_url(self):
        """Return file URL for backward compatibility."""
        return self.file.url if self.file else None
    
    def increment_views(self):
        """Increment views count."""
        self.views_count += 1
        self.save(update_fields=['views_count'])
```

### 4.2 Arquivo `apps/common/models.py`

```python
"""
Common models and mixins.
"""
from django.db import models


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created_at`` and ``updated_at`` fields.
    """
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em'
    )

    class Meta:
        abstract = True
```

## 🧪 **5. Estrutura de Testes**

### 5.1 Arquivo `pytest.ini`

```ini
[tool:pytest]
DJANGO_SETTINGS_MODULE = config.settings.testing
addopts = --verbose --tb=short --strict-markers
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    integration: marks tests as integration tests
    unit: marks tests as unit tests
```

### 5.2 Arquivo `tests/conftest.py`

```python
"""
Pytest configuration and fixtures.
"""
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
        'content_type': 'video',
        'is_public': True,
        'status': 'published'
    }
```

### 5.3 Arquivo `apps/content/tests/test_models.py`

```python
"""
Tests for content models.
"""
import pytest
from django.contrib.auth.models import User
from apps.content.models import Content, ContentType, ContentStatus


@pytest.mark.django_db
class TestContentModel:
    """Test Content model."""
    
    def test_create_content(self, user):
        """Test content creation."""
        content = Content.objects.create(
            title='Test Video',
            description='Test description',
            content_type=ContentType.VIDEO,
            creator=user
        )
        
        assert content.title == 'Test Video'
        assert content.creator == user
        assert content.status == ContentStatus.DRAFT
        assert content.views_count == 0
        assert str(content) == 'Test Video'
    
    def test_increment_views(self, user):
        """Test views increment."""
        content = Content.objects.create(
            title='Test Video',
            creator=user
        )
        
        initial_views = content.views_count
        content.increment_views()
        
        assert content.views_count == initial_views + 1
```

### 5.4 Arquivo `apps/content/tests/test_views.py`

```python
"""
Tests for content views.
"""
import pytest
from django.urls import reverse
from rest_framework import status
from apps.content.models import Content


@pytest.mark.django_db
class TestContentViewSet:
    """Test Content ViewSet."""
    
    def test_list_contents(self, api_client, user):
        """Test listing contents."""
        # Create test content
        Content.objects.create(
            title='Public Content',
            creator=user,
            is_public=True,
            status='published'
        )
        
        url = reverse('content-list')
        response = api_client.get(url)
        
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 1
    
    def test_create_content_authenticated(self, authenticated_client, content_data):
        """Test creating content when authenticated."""
        url = reverse('content-list')
        response = authenticated_client.post(url, content_data)
        
        assert response.status_code == status.HTTP_201_CREATED
        assert Content.objects.count() == 1
    
    def test_create_content_unauthenticated(self, api_client, content_data):
        """Test creating content without authentication."""
        url = reverse('content-list')
        response = api_client.post(url, content_data)
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
```

## 🐳 **6. Configuração Docker**

### 6.1 Arquivo `docker/Dockerfile`

```dockerfile
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements/ /app/requirements/
RUN pip install --no-cache-dir -r requirements/development.txt

# Copy project
COPY . /app/

# Copy entrypoint script
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Create non-root user
RUN adduser --disabled-password --gecos '' appuser
RUN chown -R appuser:appuser /app
USER appuser

ENTRYPOINT ["/entrypoint.sh"]
```

### 6.2 Arquivo `docker/docker-compose.yml`

```yaml
version: '3.8'

services:
  web:
    build:
      context: ..
      dockerfile: docker/Dockerfile
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - ..:/app
    ports:
      - "8000:8000"
    environment:
      - DJANGO_SETTINGS_MODULE=config.settings.development
    depends_on:
      - db
      - redis
    env_file:
      - ../.env

  db:
    image: postgres:14
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    environment:
      - POSTGRES_DB=streaming_db
      - POSTGRES_USER=streaming_user
      - POSTGRES_PASSWORD=streaming_pass
    ports:
      - "5432:5432"

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  postgres_data:
```

### 6.3 Arquivo `docker/entrypoint.sh`

```bash
#!/bin/bash

# Wait for database
echo "Waiting for database..."
while ! pg_isready -h db -p 5432 -U streaming_user; do
  sleep 1
done
echo "Database is ready!"

# Run migrations
python manage.py migrate

# Create superuser if it doesn't exist
python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Superuser created')
"

# Execute the command
exec "$@"
```

## 📋 **7. Arquivos de Configuração**

### 7.1 Arquivo `.env.example`

```env
# Django Settings
SECRET_KEY=your-super-secret-key-here
DEBUG=True
ALLOWED_HOST=localhost

# Database
DB_NAME=streaming_db
DB_USER=streaming_user
DB_PASSWORD=streaming_pass
DB_HOST=localhost
DB_PORT=5432

# Redis
REDIS_URL=redis://127.0.0.1:6379/1

# Sentry (Production)
SENTRY_DSN=

# Email
EMAIL_HOST=
EMAIL_PORT=587
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_USE_TLS=True
```

### 7.2 Arquivo `.gitignore`

```gitignore
# Django
*.log
*.pot
*.pyc
__pycache__/
local_settings.py
db.sqlite3
media/
staticfiles/

# Environment variables
.env

# Testing
.coverage
.pytest_cache/
htmlcov/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Docker
.dockerignore
```

### 7.3 Arquivo `.pre-commit-config.yaml`

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black
        language_version: python3.11

  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort

  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
        additional_dependencies: [flake8-docstrings]
```

## 📚 **8. Guia de Implementação**

### 8.1 Passos para Implementação

1. **Criar nova estrutura de diretórios**
   ```bash
   mkdir -p streaming_platform_v2/{config/settings,apps/{authentication,content,playlists,users,common},requirements,docker,tests,static,media}
   ```

2. **Configurar ambiente virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate  # Windows
   ```

3. **Instalar dependências**
   ```bash
   pip install -r requirements/development.txt
   ```

4. **Configurar variáveis de ambiente**
   ```bash
   cp .env.example .env
   # Editar .env com suas configurações
   ```

5. **Executar com Docker**
   ```bash
   cd docker
   docker-compose up --build
   ```

6. **Executar testes**
   ```bash
   pytest
   ```

7. **Configurar pre-commit**
   ```bash
   pre-commit install
   ```

### 8.2 Migração do Código Existente

1. **Mover modelos para apps específicos**
2. **Refatorar views usando CBV**
3. **Atualizar serializers com validações**
4. **Migrar URLs para estrutura modular**
5. **Adicionar testes para funcionalidades existentes**

## ✅ **9. Checklist de Verificação**

- [ ] Dependências atualizadas
- [ ] Estrutura multi-app criada
- [ ] Configurações separadas por ambiente
- [ ] Modelos refatorados com boas práticas
- [ ] Testes básicos implementados
- [ ] Docker configurado
- [ ] Documentação atualizada
- [ ] Pre-commit hooks configurados
- [ ] Variáveis de ambiente configuradas
- [ ] Migrações funcionando

## 🎯 **Próximos Passos (Fase 2)**

- Implementar autenticação JWT
- Adicionar rate limiting
- Configurar CI/CD
- Implementar validações avançadas
- Adicionar middleware customizado

---

Esta implementação da Fase 1 moderniza significativamente o projeto, estabelecendo uma base sólida para as próximas fases do roadmap.