# Projeto Back-End 

**Código da Disciplina**: IBM8936<br>

## Sobre 
Descreva o seu projeto em linhas gerais. 

## Instalação 
**Linguagens**: Python, Django<br>
**Tecnologias**: Github, Visual Studio Code<br>
 os pré-requisitos para rodar o seu projeto são UX, Engenharia de Dados, POO.


## Fase 2 — Autenticação e Setup (Resumo)

Esta fase adiciona autenticação JWT com refresh tokens e blacklist, uso de um modelo de usuário customizado e passos para aplicar migrações e executar os testes.

Passos rápidos:

- Definir o `AUTH_USER_MODEL` em `config/settings/development.py` (ex.: `AUTH_USER_MODEL = 'apps.users.User'`).
- Instalar dependências: `djangorestframework-simplejwt` e adicionar `rest_framework_simplejwt.token_blacklist` em `INSTALLED_APPS`.
- Executar migrações:

```pwsh
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements/development.txt
python manage.py makemigrations
python manage.py migrate
```

- Rodar teste rápido de autenticação:

```pwsh
python -m pytest src/tests/test_auth.py -q
```

Para instruções detalhadas veja `docs/fase2.md`.

