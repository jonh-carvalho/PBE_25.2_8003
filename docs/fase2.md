# Fase 2 — Autenticação JWT e Setup (Documentação)

Este documento descreve passo-a-passo a configuração necessária para a Fase 2: autenticação via JWT com refresh tokens, blacklist (logout seguro), uso do modelo User customizado e comandos de deploy/test local.

## Objetivos

- Configurar `AUTH_USER_MODEL` para o modelo customizado `apps.users.User`.
- Habilitar JWT com `djangorestframework-simplejwt` e `token_blacklist`.
- Garantir migrações corretas e disponíveis.
- Executar a bateria de testes (pytest) e comandos de deploy (Docker local / Gunicorn).

## 1) Dependências

Adicione as dependências (se ainda não estiverem no `requirements`):

- djangorestframework
- djangorestframework-simplejwt>=5.0.0
- drf-spectacular (opcional, para documentação)

No `requirements/development.txt` ou `requirements/base.txt`:

```
# Exemplo
-djangorestframework
-djangorestframework-simplejwt>=5.0.0
-rest-framework-spectacular
```

Instale no ambiente virtual:

```pwsh
pip install djangorestframework djangorestframework-simplejwt drf-spectacular
```

## 2) Configuração do modelo de usuário

1. Garanta que o aplicativo `apps.users` tenha o modelo `User` baseado em `AbstractUser` (arquivo: `apps/users/models.py`).
2. Em `config/settings/development.py` (ou no settings do ambiente em uso) defina:

```python
AUTH_USER_MODEL = 'apps.users.User'
```

3. Se você já tinha rodado migrações antes de trocar o `AUTH_USER_MODEL`, recrie as migrações ou aplique um novo banco de dados. Trocar `AUTH_USER_MODEL` em um projeto com migrações já aplicadas requer migração cuidadosa ou recriação do banco de dados.

Notas:
- Sempre usar `django.contrib.auth.get_user_model()` em código e `settings.AUTH_USER_MODEL` em ForeignKey para evitar import hard-coded.

## 3) Configuração do SimpleJWT e token_blacklist

1. Em `config/settings/base.py` (ou `development.py`) adicione:

```python
INSTALLED_APPS += [
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
]

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}
```

2. Verifique se `apps.auth` (ou nome usado localmente) não conflita com o pacote `django.contrib.auth`. Se necessário, crie um `AppConfig` com `label` único (ex.: `apps_auth`) e registre-o em `INSTALLED_APPS` via `apps.auth.apps.AuthConfig`.

## 4) Migrações

1. Criar migrações para os apps modificados:

```pwsh
python manage.py makemigrations
```

2. Aplicar migrações:

```pwsh
python manage.py migrate
```

Importante:
- Se o banco contém dados e `AUTH_USER_MODEL` foi alterado, avalie recriar o banco ou migrar dados cuidadosamente.

## 5) Endpoints de autenticação

- `POST /api/auth/login/` → retorna `access` e `refresh`
- `POST /api/auth/refresh/` → renova `access` usando o `refresh`
- `POST /api/auth/logout/` → blacklist do `refresh` (requer Authorization Bearer do access token)

Exemplo de request para login:

```http
POST /api/auth/login/
Content-Type: application/json

{
  "username": "user",
  "password": "pass"
}
```

Resposta esperada:

```json
{
  "access": "<jwt-access-token>",
  "refresh": "<jwt-refresh-token>"
}
```

Logout (body): `{ "refresh": "<jwt-refresh-token>" }` com header `Authorization: Bearer <access>`.

## 6) Testes

Executar toda a suíte de testes (use o venv criado no projeto):

```pwsh
# ativar venv (Windows PowerShell)
.\.venv\Scripts\Activate.ps1
pip install -r requirements/development.txt
python -m pytest -q
```

Para rodar apenas testes de autenticação:

```pwsh
python -m pytest src/tests/test_auth.py -q
```

## 7) Deploy local com Docker (exemplo)

Arquivo `docker/Dockerfile` e `docker/docker-compose.yml` devem estar presentes. Passos:

```pwsh
cd F:\Apps\source\repos\25.2\PBE_25.2_8003\Refactor_Streaming\Fases\fase1
# build and start
docker compose up --build -d
# aplicar migrações dentro do container
docker compose exec web python manage.py migrate
# criar superuser (opcional)
docker compose exec web python manage.py createsuperuser
```

## 8) Checklist de verificação

- [ ] `AUTH_USER_MODEL` definido corretamente
- [ ] `rest_framework_simplejwt.token_blacklist` em `INSTALLED_APPS`
- [ ] Migrations criadas e aplicadas
- [ ] Endpoints `login/refresh/logout` funcionando
- [ ] Testes passando

## 9) Proximos passos sugeridos

- Adicionar CI (GitHub Actions) que execute: `pip install -r requirements/development.txt`, `python manage.py migrate --noinput`, `pytest`.
- Remover artefatos de debug (`src/tests/test_debug_token.py` e `src/scripts/debug_login.py`) antes do merge final.
- Documentar decisões (por que usamos ROTATE_REFRESH_TOKENS, tempo de expiração, etc.).

---

Se quiser, eu atualizo o `README.md` com um changelog mais detalhado e removo os artefatos de debug e ainda crio um workflow de CI simples.