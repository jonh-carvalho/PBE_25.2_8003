---
id: diagrama_de_classes
title: Diagrama de Classes Conceitual
---

## Diagrama de Classes Conceitual

### Descrição

Este diagrama apresenta as principais classes conceituais do sistema de rede social, baseado nos casos de uso identificados na fase de elaboração.

### Classes Identificadas

#### **Usuario**
- **Atributos:**
  - id: Integer
  - email: String
  - senha: String (encriptada)
  - dataCreacao: DateTime
  - dataUltimoAcesso: DateTime
  - status: Enum (Ativo, Inativo, Pendente)
  - emailVerificado: Boolean

- **Responsabilidades:**
  - Gerenciar autenticação do usuário
  - Manter dados básicos da conta
  - Controlar status da conta

#### **Perfil**
- **Atributos:**
  - id: Integer
  - nome: String
  - sobrenome: String
  - bio: String
  - foto: String (URL)
  - dataNascimento: Date
  - privacidade: Enum (Publico, Privado, Amigos)

- **Responsabilidades:**
  - Armazenar informações pessoais do usuário
  - Gerenciar configurações de privacidade
  - Exibir informações para outros usuários

#### **Postagem**
- **Atributos:**
  - id: Integer
  - conteudo: String
  - dataPostagem: DateTime
  - tipoPostagem: Enum (Texto, Imagem, Video)
  - visibilidade: Enum (Publico, Amigos, Privado)
  - qtdLikes: Integer
  - qtdComentarios: Integer

- **Responsabilidades:**
  - Armazenar conteúdo público do usuário
  - Gerenciar interações (likes, comentários)
  - Controlar visibilidade da postagem

#### **Mensagem**
- **Atributos:**
  - id: Integer
  - conteudo: String
  - dataEnvio: DateTime
  - lida: Boolean
  - tipoMensagem: Enum (Texto, Imagem, Arquivo)

- **Responsabilidades:**
  - Gerenciar comunicação privada entre usuários
  - Controlar status de leitura
  - Armazenar diferentes tipos de conteúdo

#### **Comentario**
- **Atributos:**
  - id: Integer
  - conteudo: String
  - dataComentario: DateTime
  - qtdLikes: Integer

- **Responsabilidades:**
  - Permitir interação em postagens
  - Manter histórico de comentários

#### **Relacionamento**
- **Atributos:**
  - id: Integer
  - dataInicio: DateTime
  - status: Enum (Seguindo, Amigo, Bloqueado)
  - tipoRelacionamento: Enum (Seguidor, Amigo)

- **Responsabilidades:**
  - Gerenciar conexões entre usuários
  - Controlar tipos de relacionamento

#### **Galeria**
- **Atributos:**
  - id: Integer
  - nome: String
  - descricao: String
  - dataCriacao: DateTime
  - privacidade: Enum (Publico, Privado, Amigos)

- **Responsabilidades:**
  - Organizar coleções de mídia
  - Gerenciar álbuns de fotos/vídeos

#### **Grupo**
- **Atributos:**
  - id: Integer
  - nome: String
  - descricao: String
  - dataCriacao: DateTime
  - tipoGrupo: Enum (Publico, Privado, Restrito)
  - qtdMembros: Integer

- **Responsabilidades:**
  - Facilitar comunicação em grupo
  - Gerenciar membros e permissões

### Relacionamentos Principais

1. **Usuario 1:1 Perfil** - Cada usuário possui um perfil
2. **Usuario 1:* Postagem** - Um usuário pode criar várias postagens
3. **Usuario *:* Relacionamento** - Usuários podem ter múltiplos relacionamentos
4. **Postagem 1:* Comentario** - Uma postagem pode ter vários comentários
5. **Usuario 1:* Comentario** - Um usuário pode fazer vários comentários
6. **Usuario 1:* Mensagem** (como remetente) - Um usuário pode enviar várias mensagens
7. **Usuario 1:* Mensagem** (como destinatário) - Um usuário pode receber várias mensagens
8. **Usuario 1:* Galeria** - Um usuário pode ter várias galerias
9. **Usuario *:* Grupo** - Usuários podem participar de múltiplos grupos

### Diagrama UML (Representação Textual)

```
[Usuario]
- id: Integer
- email: String
- senha: String
- dataCreacao: DateTime
- status: Enum
+ autenticar()
+ alterarSenha()
+ excluirConta()

[Perfil]
- id: Integer
- nome: String
- bio: String
- foto: String
+ editarPerfil()
+ visualizarPerfil()

[Postagem]
- id: Integer
- conteudo: String
- dataPostagem: DateTime
- visibilidade: Enum
+ criarPostagem()
+ excluirPostagem()
+ interagir()

Usuario ||--|| Perfil : possui
Usuario ||--o{ Postagem : cria
Usuario }o--o{ Relacionamento : participa
Postagem ||--o{ Comentario : recebe
Usuario ||--o{ Comentario : faz
```

### Regras de Negócio Principais

1. Todo usuário deve ter um email único no sistema
2. Perfis podem ser públicos ou privados
3. Postagens podem ter diferentes níveis de visibilidade
4. Mensagens são sempre privadas entre dois usuários
5. Relacionamentos podem ser unidirecionais (seguir) ou bidirecionais (amizade)
6. Grupos podem ter diferentes tipos de acesso e moderação
