# API Cadastro de Funcionários em Django Rest Framework
Uma API simples em **Django Rest Framewor** para um cadastro de Funcionários.</br>
A idéia é fornecer o acesso da API aos usuários cadastrados, protegendo os dados sensíveis</br>
de acessos indevidos e pessoas não autorizadas, utilizando o sistema de autenticação via token com JWT.</br>
Usuários não administradores podem ter acesso de leitura, criação e alteração de dados.</br>
Somente usuários Administradores podem excluir um cadastro.</br>
Os dados são fictícios e gerados com o Faker.</br>

###### Para ver esta API funcionando na internet acesse: Em Breve(mudando o provedor)

## Este projeto foi feito com:

* [Python 3.10.1](https://www.python.org/)
* [Django 4.1](https://www.djangoproject.com/)
* [Django Rest Framework 3.13.1](https://getbootstrap.com/)

## Como rodar o projeto localmente?

* Clone esse repositório.
* Crie um virtualenv com Python 3.10.1 no mínimo.
* Ative a virtualenv.
* Instale as dependências listadas em requirements.txt.
* Banco de dados é o padrão do Django(db.sqlite3)
* Crie um Super Usuário e depois de migrar, crie um usuário comum
* Rode as migrações.
* Configure seu .env(exemplo em .env_config)
* Popule a tabela com dados fictícios(populate_table)

git clone https://github.com/fspjonny/funcionarios_rest_api.git<br>
cd funcionarios_rest_api<br>
python -m venv venv<br>
pip install -r requirements.txt<br>
python manage.py migrate<br>
python manage.py populate_table<br>
python manage.py runserver<br>