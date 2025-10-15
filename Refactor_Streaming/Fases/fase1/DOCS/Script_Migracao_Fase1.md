# 🔄 Script de Migração - Fase 1

Este script automatiza a migração do projeto antigo para a nova estrutura da Fase 1.

## 📋 Pré-requisitos

- Python 3.11+
- Git instalado
- Docker instalado (opcional)

## 🚀 Executando a Migração

### 1. Preparação do Ambiente

```bash
# 1. Fazer backup do projeto atual
cp -r streaming_platform streaming_platform_backup

# 2. Criar nova estrutura
mkdir streaming_platform_v2
cd streaming_platform_v2

# 3. Inicializar Git (se necessário)
git init
```

### 2. Criar Estrutura de Diretórios

```bash
# Criar estrutura base
mkdir -p config/settings
mkdir -p apps/{authentication,content,playlists,users,common}
mkdir -p requirements
mkdir -p docker
mkdir -p tests/integration
mkdir -p static
mkdir -p media

# Criar arquivos __init__.py
touch config/__init__.py
touch apps/__init__.py
touch apps/{authentication,content,playlists,users,common}/__init__.py
touch tests/__init__.py
```

### 3. Configurar Dependências

```bash
# Criar requirements
cat > requirements/base.txt << 'EOF'
Django>=4.2.0,<5.0
djangorestframework>=3.14.0
drf-spectacular>=0.26.0
django-cors-headers>=4.0.0
python-decouple>=3.8
python-dotenv>=1.0.0
psycopg2-binary>=2.9.0
Pillow>=10.0.0
django-extensions>=3.2.0
EOF

cat > requirements/development.txt << 'EOF'
-r base.txt
django-debug-toolbar>=4.1.0
ipython>=8.12.0
pytest>=7.4.0
pytest-django>=4.5.0
pytest-cov>=4.1.0
factory-boy>=3.2.0
black>=23.0.0
isort>=5.12.0
flake8>=6.0.0
mypy>=1.4.0
django-stubs>=4.2.0
pre-commit>=3.3.0
EOF

cat > requirements/production.txt << 'EOF'
-r base.txt
gunicorn>=21.0.0
redis>=4.6.0
django-redis>=5.3.0
sentry-sdk>=1.28.0
django-ratelimit>=4.0.0
EOF
```

### 4. Configurar Ambiente Virtual

```bash
# Criar e ativar ambiente virtual
python -m venv venv

# Ativar (Linux/Mac)
source venv/bin/activate

# Ativar (Windows)
# venv\Scripts\activate

# Instalar dependências
pip install -r requirements/development.txt
```

### 5. Migrar Modelos

```bash
# Copiar e adaptar modelos do projeto antigo
# Exemplo para Content:

# 1. Copiar modelo original
cp ../streaming_platform/content_app/models.py apps/content/models.py

# 2. Atualizar imports e adicionar melhorias
# (usar o exemplo fornecido no roadmap)
```

### 6. Configurar Settings

```bash
# Criar arquivo de configuração base
cat > config/settings/base.py << 'EOF'
# (usar o conteúdo do exemplo fornecido)
EOF

# Criar configurações de desenvolvimento
cat > config/settings/development.py << 'EOF'
# (usar o conteúdo do exemplo fornecido)
EOF

# Criar configurações de produção
cat > config/settings/production.py << 'EOF'
# (usar o conteúdo do exemplo fornecido)
EOF
```

### 7. Configurar Docker

```bash
# Criar Dockerfile
cat > docker/Dockerfile << 'EOF'
# (usar o conteúdo do exemplo fornecido)
EOF

# Criar docker-compose
cat > docker/docker-compose.yml << 'EOF'
# (usar o conteúdo do exemplo fornecido)
EOF

# Criar entrypoint
cat > docker/entrypoint.sh << 'EOF'
# (usar o conteúdo do exemplo fornecido)
EOF

chmod +x docker/entrypoint.sh
```

### 8. Configurar Variáveis de Ambiente

```bash
# Criar arquivo de exemplo
cat > .env.example << 'EOF'
SECRET_KEY=your-super-secret-key-here
DEBUG=True
ALLOWED_HOST=localhost
DB_NAME=streaming_db
DB_USER=streaming_user
DB_PASSWORD=streaming_pass
DB_HOST=localhost
DB_PORT=5432
REDIS_URL=redis://127.0.0.1:6379/1
SENTRY_DSN=
EMAIL_HOST=
EMAIL_PORT=587
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_USE_TLS=True
EOF

# Copiar para .env e ajustar valores
cp .env.example .env
```

### 9. Migrar Dados

```bash
# Executar migrações
python manage.py makemigrations
python manage.py migrate

# Importar dados do projeto antigo (se necessário)
python manage.py shell << 'EOF'
# Script para migrar dados
from django.contrib.auth.models import User
from apps.content.models import Content

# Exemplo de migração de dados
# (adaptar conforme necessário)
EOF
```

### 10. Configurar Testes

```bash
# Criar configuração pytest
cat > pytest.ini << 'EOF'
[tool:pytest]
DJANGO_SETTINGS_MODULE = config.settings.testing
addopts = --verbose --tb=short --strict-markers
markers =
    slow: marks tests as slow
    integration: marks tests as integration tests
    unit: marks tests as unit tests
EOF

# Executar testes
pytest
```

### 11. Configurar Git Hooks

```bash
# Configurar pre-commit
cat > .pre-commit-config.yaml << 'EOF'
# (usar o conteúdo do exemplo fornecido)
EOF

# Instalar hooks
pre-commit install
```

## ✅ Checklist de Verificação

Após executar a migração, verifique:

- [ ] Estrutura de diretórios criada corretamente
- [ ] Dependências instaladas sem erros
- [ ] Configurações funcionando (development/production)
- [ ] Banco de dados configurado e migrações aplicadas
- [ ] Docker funcionando (opcional)
- [ ] Testes passando
- [ ] Pre-commit hooks configurados
- [ ] Variáveis de ambiente definidas
- [ ] Dados migrados (se aplicável)

## 🔧 Solução de Problemas Comuns

### Erro de Importação de Módulos

```bash
# Adicionar diretório ao PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### Erro de Banco de Dados

```bash
# Verificar se PostgreSQL está rodando
sudo service postgresql start

# Ou usar Docker
docker-compose up db
```

### Erro de Dependências

```bash
# Limpar cache do pip
pip cache purge

# Reinstalar dependências
pip install --no-cache-dir -r requirements/development.txt
```

### Erro de Permissões (Docker)

```bash
# Ajustar permissões
sudo chown -R $USER:$USER .
```

## 📊 Comparação: Antes vs Depois

### Estrutura Antiga
```
streaming_platform/
├── manage.py
├── streaming_platform/
│   ├── settings.py
│   └── urls.py
└── content_app/
    ├── models.py
    ├── views.py
    └── urls.py
```

### Nova Estrutura
```
streaming_platform/
├── config/
│   ├── settings/
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   └── urls.py
├── apps/
│   ├── content/
│   ├── playlists/
│   ├── users/
│   └── common/
├── requirements/
├── docker/
└── tests/
```

## 🎯 Próximos Passos

Após completar a migração da Fase 1:

1. **Testar funcionamento completo**
2. **Treinar equipe na nova estrutura**
3. **Documentar mudanças**
4. **Planejar Fase 2 (JWT, Rate Limiting)**
5. **Configurar CI/CD pipeline**

## 📞 Suporte

Para dúvidas ou problemas durante a migração:

1. Consultar documentação do Django
2. Verificar logs de erro detalhadamente
3. Testar cada componente isoladamente
4. Usar Docker para ambiente padronizado