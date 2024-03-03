# S4 Suprimentos - Aplicação Web Flask

Esta é uma aplicação web Flask para cadastro de usuários, login de usuários e operações CRUD (Create, Read, Update, Delete) de produtos para uma empresa s4 Smar Supply.

## Configuração e Execução

Para configurar e executar esta aplicação, siga as instruções abaixo:

### Pré-requisitos

Certifique-se de ter instalado o Python 3 e o pip em seu ambiente de desenvolvimento.

### Instalação de Dependências

Antes de executar a aplicação, instale as dependências necessárias. No terminal, execute o seguinte comando:

- Flask: O framework web usado para construir a aplicação.
- Flask-SQLAlchemy: Uma extensão Flask que simplifica o uso do SQLAlchemy para interagir com o banco de dados.
- Flask-MySQL-Connector: Uma extensão Flask que permite conectar-se ao banco de dados MySQL.

## Criação do Banco de Dados

Esta aplicação utiliza um banco de dados MySQL. Antes de executar a aplicação, você precisa criar o banco de dados. Siga estas etapas:

1. Instale e configure o MySQL em sua máquina, se ainda não estiver configurado.
2. Crie um novo banco de dados com o nome `S4_Suprimentos`.
3. Certifique-se de ter um usuário do MySQL com permissões adequadas para acessar e manipular o banco de dados.

## Configuração da Aplicação

Edite o arquivo `app.py` para configurar a URI do banco de dados SQLAlchemy e a chave secreta do Flask.

## Execução da Aplicação

Após configurar o banco de dados e a aplicação, você pode executar a aplicação Flask. No terminal, execute o seguinte comando:

Isso iniciará o servidor Flask. Você poderá acessar a aplicação em `http://localhost:5000/`.

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte maneira:

- `app.py`: Arquivo principal da aplicação que define as rotas principais e configurações.
- `models.py`: Contém as definições dos modelos de dados para usuários e produtos, usando SQLAlchemy.
- `usuario_cadastro.py`, `usuario_login.py`, `produto_cadastro.py`, `produto_atualizar.py`, `produto_excluir.py`: Arquivos que definem as rotas e lógica de negócios relacionadas a usuários e produtos, separadas por funcionalidade.
- `templates/`: Pasta que contém os templates HTML para renderização das páginas.
- `DATABASE/`: Pasta que contém o script SQL para a criação do banco de dados e das tabelas.

## Decisões de Design

- **Blueprints**: As rotas relacionadas a usuários e produtos foram agrupadas em blueprints separados para melhor organização e modularidade do código.
- **Modelos de Dados**: Foram criados modelos de dados separados para usuários e produtos, permitindo uma estrutura mais flexível e escalável para o banco de dados.

