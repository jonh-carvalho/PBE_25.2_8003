---
id: diagrama_de_casos_de_uso
title: Diagrama de Casos de Uso
---

## Diagrama de Casos de Uso

### Visão Geral do Sistema

Este diagrama apresenta os principais casos de uso do sistema de rede social, organizados por módulos funcionais e seus respectivos atores.

### Atores do Sistema

- **Usuário**: Pessoa que utiliza o sistema
- **Sistema**: Sistema automatizado que executa validações e processamentos
- **Administrador**: Usuário com privilégios especiais para gerenciar o sistema

### Módulos e Casos de Uso

#### **Módulo: Gerenciamento de Contas**
- **UC01 - Criação de Conta**
- **UC02 - Login no Sistema**
- **UC03 - Alteração de Dados da Conta**
- **UC04 - Recuperar Senha**
- **UC05 - Exclusão Lógica de Conta**
- **UC06 - Visualização de Conta**

#### **Módulo: Gerenciamento de Perfis**
- **UC07 - Edição de Perfil**
- **UC08 - Pesquisar Perfis**
- **UC09 - Visualização de Perfil**
- **UC10 - Seguir Usuário**
- **UC11 - Deixar de Seguir Usuário**
- **UC12 - Bloquear Usuário**

#### **Módulo: Postagens Públicas**
- **UC13 - Criar Postagem**
- **UC14 - Excluir Postagem**
- **UC15 - Curtir Postagem**
- **UC16 - Comentar Postagem**
- **UC17 - Compartilhar Postagem**
- **UC18 - Visualizar Feed**

#### **Módulo: Mensagens Privadas**
- **UC19 - Enviar Mensagem**
- **UC20 - Excluir Mensagem**
- **UC21 - Visualizar Conversas**
- **UC22 - Marcar Mensagem como Lida**

#### **Módulo: Galerias e Mídias**
- **UC23 - Criar Álbum**
- **UC24 - Adicionar Foto ao Álbum**
- **UC25 - Remover Foto do Álbum**
- **UC26 - Visualizar Galeria**

#### **Módulo: Grupos**
- **UC27 - Criar Grupo**
- **UC28 - Participar de Grupo**
- **UC29 - Sair de Grupo**
- **UC30 - Postar em Grupo**

### Representação UML (Textual)

```
    [Usuário]
        |
        |---(UC01) Criação de Conta
        |---(UC02) Login no Sistema
        |---(UC03) Alteração de Dados
        |---(UC04) Recuperar Senha
        |---(UC07) Edição de Perfil
        |---(UC08) Pesquisar Perfis
        |---(UC09) Visualizar Perfil
        |---(UC10) Seguir Usuário
        |---(UC13) Criar Postagem
        |---(UC15) Curtir Postagem
        |---(UC16) Comentar Postagem
        |---(UC18) Visualizar Feed
        |---(UC19) Enviar Mensagem
        |---(UC21) Visualizar Conversas
        |---(UC23) Criar Álbum
        |---(UC27) Criar Grupo
        
    [Sistema]
        |
        |---(UC01) Criação de Conta <<include>>
        |---(UC02) Login no Sistema <<include>>
        |---(UC04) Recuperar Senha <<include>>
```

### Relacionamentos Entre Casos de Uso

- **Include**: Casos de uso que sempre são executados
  - UC01 (Criação de Conta) <<include>> Validar Email
  - UC02 (Login) <<include>> Autenticar Usuário
  - UC13 (Criar Postagem) <<include>> Validar Conteúdo

- **Extend**: Casos de uso opcionais
  - UC09 (Visualizar Perfil) <<extend>> UC10 (Seguir Usuário)
  - UC18 (Visualizar Feed) <<extend>> UC15 (Curtir Postagem)
  - UC18 (Visualizar Feed) <<extend>> UC16 (Comentar Postagem)

---

## Especificações Detalhadas dos Casos de Uso

### UC01 - Criação de Conta no Sistema

**Atores:**
- Usuário (primário)
- Sistema (secundário)

**Pré-condições:**
- Nenhuma

**Fluxo Principal:**
1. Usuário fornece e-mail, senha e confirmação de senha
2. Sistema valida formato do e-mail
3. Sistema verifica se e-mail não está em uso
4. Sistema valida regras de segurança da senha
5. Sistema encripta a senha
6. Sistema persiste os dados do usuário
7. Sistema gera link de verificação com prazo de expiração
8. Sistema envia e-mail de verificação para o usuário
9. Usuário acessa o link de verificação
10. Sistema ativa a conta
11. Sistema exibe mensagem de sucesso
12. Sistema redireciona para página de login

**Fluxos Alternativos:**
- **2a.** E-mail com formato inválido:
  - 2a1. Sistema exibe mensagem de erro
  - 2a2. Retorna ao passo 1
- **3a.** E-mail já está em uso:
  - 3a1. Sistema exibe mensagem informando que e-mail já existe
  - 3a2. Retorna ao passo 1
- **4a.** Senha não atende aos critérios de segurança:
  - 4a1. Sistema exibe critérios não atendidos
  - 4a2. Retorna ao passo 1
- **9a.** Link de verificação expirado:
  - 9a1. Sistema exibe mensagem de link expirado
  - 9a2. Sistema oferece opção de reenviar e-mail

**Pós-condições:**
- Conta criada e ativa no sistema
- Usuário pode fazer login

---

### UC02 - Login no Sistema

**Atores:**
- Usuário (primário)
- Sistema (secundário)

**Pré-condições:**
- Usuário deve ter conta criada e verificada

**Fluxo Principal:**
1. Usuário fornece e-mail e senha
2. Sistema valida credenciais
3. Sistema autentica o usuário
4. Sistema cria sessão de usuário
5. Sistema redireciona para página inicial

**Fluxos Alternativos:**
- **2a.** Credenciais inválidas:
  - 2a1. Sistema exibe mensagem de erro
  - 2a2. Sistema incrementa contador de tentativas
  - 2a3. Retorna ao passo 1
- **2b.** Muitas tentativas de login:
  - 2b1. Sistema bloqueia temporariamente a conta
  - 2b2. Sistema envia e-mail de notificação
- **3a.** Primeiro acesso do usuário:
  - 3a1. Sistema redireciona para página de edição de perfil

**Pós-condições:**
- Usuário autenticado no sistema
- Sessão ativa criada

---

### UC13 - Criar Postagem

**Atores:**
- Usuário (primário)
- Sistema (secundário)

**Pré-condições:**
- Usuário deve estar autenticado
- Usuário deve ter perfil completo

**Fluxo Principal:**
1. Usuário acessa funcionalidade de criar postagem
2. Usuário insere conteúdo da postagem
3. Usuário seleciona tipo de mídia (opcional)
4. Usuário define configurações de privacidade
5. Sistema valida conteúdo
6. Sistema processa mídia (se houver)
7. Sistema salva a postagem
8. Sistema publica no feed dos seguidores
9. Sistema exibe confirmação de publicação

**Fluxos Alternativos:**
- **3a.** Usuário adiciona imagem:
  - 3a1. Sistema valida formato e tamanho
  - 3a2. Sistema processa e otimiza imagem
- **3b.** Usuário adiciona vídeo:
  - 3b1. Sistema valida formato e duração
  - 3b2. Sistema processa vídeo
- **5a.** Conteúdo contém palavras inadequadas:
  - 5a1. Sistema solicita revisão do conteúdo
  - 5a2. Retorna ao passo 2

**Pós-condições:**
- Postagem criada e visível conforme configurações de privacidade
- Seguidores podem visualizar no feed

---

### UC19 - Enviar Mensagem

**Atores:**
- Usuário (primário)
- Destinatário (secundário)
- Sistema (secundário)

**Pré-condições:**
- Usuário deve estar autenticado
- Destinatário deve existir no sistema
- Usuário não deve estar bloqueado pelo destinatário

**Fluxo Principal:**
1. Usuário seleciona destinatário
2. Usuário escreve mensagem
3. Sistema valida conteúdo da mensagem
4. Sistema verifica permissões de privacidade
5. Sistema envia mensagem
6. Sistema notifica destinatário
7. Sistema exibe confirmação de envio

**Fluxos Alternativos:**
- **4a.** Destinatário tem perfil privado e não segue o usuário:
  - 4a1. Sistema exibe mensagem sobre restrições de privacidade
  - 4a2. Sistema oferece opção de enviar solicitação de conexão
- **6a.** Destinatário está offline:
  - 6a1. Sistema armazena notificação para entrega posterior

**Pós-condições:**
- Mensagem enviada e armazenada
- Destinatário notificado (se online) ou notificação agendada

### Criação de uma conta no sistema

* Atores:

	- Usuário
	- Sistema

- Pré-Condições:
	- Nenhuma

* Fluxo Básico:
    1. Usuário fornece e-mail, senha e confirmações
    2. Dados do Usuário são validados pelo Sistema
    3. Dados do Usuário são encriptados pelo Sistema
    4. Dados do Usuário são persistidos pelo Sistema
    5. Sistema gera um link com prazo de expiração
    6. Sistema envia e-mail de verificação, com o link, para o Usuário
    7. Usuário confirma o e-mail antes do link expirar
    8. Sistema confirma que o Cadastro do Usuário foi realizado com sucesso
    9. Sistema redireciona o Usuário para a página de Entrada

- Fluxos Alternativos:
	- 2a. E-mail do Usuário é inválido
		2a1. Sistema exibe mensagem de erro
	- 2b. Senha do Usuário não respeita regras de segurança
		- 2b1. Sistema exibe mensagem de erro
	- 3a. Usuário tenta confirmar o e-mail depois de o link expirar
		- 3a1. Sistema sugere que o Usuário realize um novo Cadastro

### Entrada do usuário no sistema

- Atores:
	- Usuário
	- Sistema

- Pré-Condições:
	Usuário deve estar cadastrado

- Fluxo Básico:
    - 1. Usuário fornece e-mail e senha
	- 2. Sistema autentica o Usuário
	- 3. Sistema redireciona o Usuário para a página inicial

- Fluxos Alternativos:
	- 2a. Dados do Usuário Inválidos
		- 2a1. Sistema exibe mensagem de erro
	- 3a. Primeio acesso do Usuário
		- 3a1. Sistema redireciona o Usuário para a página de edição de perfil
