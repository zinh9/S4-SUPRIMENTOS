# S4 Suprimentos - Aplicação Web Flask

Esta é uma aplicação web Flask para cadastro de usuários, login de usuários e operações CRUD (Create, Read, Update, Delete) de produtos para uma empresa s4 Smar Supply.

## Configuração e Execução

Para configurar e executar esta aplicação, siga as instruções abaixo:

### Pré-requisitos

- Certifique-se de ter instalado o Python 3 e o pip em seu ambiente de desenvolvimento.
- Ter o banco de dados MySQL para ser conectado pelo SQLAlchemy para que a aplicação possa interagir com os dados armazenados.

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

Após configurar o banco de dados e a aplicação, você pode executar a aplicação Flask. No terminal, execute o seguinte comando: `py app.py`

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

## Padrão MVC

1. Model: As definições de modelos de dados para usuários e produtos estão localizadas no arquivo models.py. Esses modelos representam a   camada de modelo no padrão MVC, responsável por lidar com a lógica de negócios e a manipulação de dados.

2. View: Os templates HTML para renderização das páginas estão armazenados na pasta templates/. Esses arquivos representam a camada de visualização no padrão MVC, responsável por apresentar os dados aos usuários.

3. Controller: As rotas e a lógica de negócios relacionadas a usuários e produtos estão definidas nos arquivos usuario_cadastro.py, usuario_login.py, produto_cadastro.py, produto_atualizar.py e produto_excluir.py. Esses arquivos representam a camada de controle no padrão MVC, responsável por receber solicitações do usuário, processar essas solicitações e fornecer uma resposta adequada.

## Padrões de API RESTful

1. Recursos Claros e Identificáveis: Os recursos dentro da aplicação, como usuários e produtos, são claramente definidos nos modelos Usuario e Produto, respectivamente. Cada recurso é identificado de forma única e possui atributos que o caracterizam.

2. Métodos HTTP Semânticos: Os métodos HTTP são utilizados de acordo com as operações CRUD (Create, Read, Update, Delete) nos recursos.

3. Uso de URIs Descritivas: As URIs seguem uma estrutura descritiva e semântica, o que facilita o entendimento e a navegação na API.

## Uso do PEP-8

O código segue as diretrizes de estilo de codificação definidas no PEP-8, que é o guia de estilo para o código Python. Isso garante consistência e legibilidade no código fonte, facilitando a manutenção e colaboração entre desenvolvedores.
