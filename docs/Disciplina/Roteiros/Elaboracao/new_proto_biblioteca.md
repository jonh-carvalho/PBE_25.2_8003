# Protótipo de Baixa Fidelidade - Biblioteca Digital

## Introdução

Este documento apresenta o protótipo de baixa fidelidade para o sistema de biblioteca de livros digitais, auxiliando na definição da interface, funcionalidades e fluxo de navegação para validação inicial com usuários e equipe de desenvolvimento.

## Metodologia

O protótipo foi elaborado com base nos requisitos levantados e nos casos de uso principais, utilizando ferramentas como papel, lápis e software de prototipação simples. O objetivo é validar a experiência do usuário, fluxo de telas e principais funcionalidades antes da implementação.

## Telas do Protótipo

- Tela de Login
- Tela de Cadastro
- Tela de Busca de Livros
- Tela de Detalhes do Livro
- Tela de Reserva de Livro
- Tela de Download
- Tela de Perfil do Usuário
- Tela de Assinatura Premium
- Tela de Notificações

## Diagrama de Navegação (Salt/PlantUML)

```plantuml
@startsalt
{
  + "Login"
  + "Cadastro"
  + "Feed de Livros"
  + "Detalhes do Livro"
  + "Reserva"
  + "Download"
  + "Perfil"
  + "Assinatura Premium"
  + "Notificações"
}
@endsalt
```

## Tela de Login

```plantuml
@startsalt
{+
  {
   **Biblioteca Digital**
   .
    "E-mail" 
    "Senha"
    
    .
    [ "Entrar" ]
    [ "Cadastrar" ]
    [ "Esqueceu a senha?" ]
  }
}
@endsalt
```

## Tela de Cadastro

```plantuml
@startsalt
{+
  {
    Cadastro de Usuário
     "Nome"
     "E-mail"
     "Senha"
     "Confirmar Senha"
    ["Cadastrar"]
    [ "Voltar ao Login" ]
  }
}
@endsalt
```

## Tela de Feed de Livros

```
@startsalt
{+
  {
    " Autor, Título,... " | [ Barra de Busca ]
    {+
    () Feed de Livros | [Detalhes]  
    () Feed de Livros
    .
    () Feed de Livros
    }

    [ "Perfil" ]
    [ "Assinatura" ]
    [ "Notificações" ]
  }
}
@endsalt
```

## Tela de Detalhes do Livro

```plantuml
@startsalt
{
  {+
    Detalhes do Livro
    Capa
    Título: " ... " |  Autor: " ... "
    Categoria: " ..." | Formato: " ..."
    Status: "..." 
    [ "Reservar" ]
    [ "Baixar" ]
    [ "Voltar" ]
  }
}
@endsalt
```


## Tela de Reserva

```plantuml
@startsalt
{
  {
    Reserva de Livro |  
    .
    "Livro"
    "Prazo de Retirada"
    [ "Confirmar Reserva" ]
    [ "Cancelar" ]
  }
}
@endsalt
```

## Tela de Download

```plantuml
@startsalt
{
  {
    "Download de Livro"
    [ "Arquivo" ]
    [ "Formato" ]
    [ "Baixar" ]
    [ "Voltar" ]
  }
}
@endsalt
```

## Tela de Perfil do Usuário

```plantuml
@startsalt
{
  {
    "Perfil do Usuário"
    [ "Nome" ]
    [ "E-mail" ]
    [ "Assinatura" ]
    [ "Histórico de Reservas" ]
    [ "Editar Perfil" ]
    [ "Sair" ]
  }
}
@endsalt
```

## Tela de Assinatura Premium

```plantuml
@startsalt
{
  {
    "Assinatura Premium"
    [ "Tipo de Plano" ]
    [ "Benefícios" ]
    [ "Assinar/Renovar" ]
    [ "Voltar" ]
  }
}
@endsalt
```

## Tela de Notificações

```plantuml
@startsalt
{
  {
    "Notificações"
    [ "Lista de Mensagens" ]
    [ "Marcar como lida" ]
    [ "Voltar" ]
  }
}
@endsalt
```

## Conclusão

O protótipo de baixa fidelidade permite validar o fluxo principal do sistema, identificar melhorias na interface e garantir que os requisitos essenciais estejam contemplados antes do desenvolvimento detalhado.

## Referências

- Documento de requisitos da biblioteca digital
- Ferramentas de prototipação (ex: Figma, papel e lápis)
- Material Design Color Tool
