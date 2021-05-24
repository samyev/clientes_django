# Clientes Django

Esta é uma básica aplicação feita em django para cadastro de clientes, com ela você pode criar, editar e deletar clientes.

## Requisitos 

- Python 3.8.6
- Pip 21.1.1 (pip3)
- Virtualenv 20.4.6
- Django 3.2.3
- Vscode 1.56.2


## Como Utilizar

Para iniciar a aplicação, primeiramente você deve obter todos os requisitos listados a cima. Abra o repositório do projeto no terminal, neste caso **clientes_django/**, depois deve-se iniciar a sua virtualenv:

~~~ Bash
source venv/bin/activate
~~~

Em seguida, ainda no terminal, entre na pasta **clientes_django/projeto/**

~~~ Bash
cd projeto/
~~~

Para iniciar a plicação utiliza o comando a baixo:

~~~ Bash
python3 manage.py runserver
~~~

O comando a cima irá executar a aplicação na porta 8080, caso esta porta já esteja ocupada na sua máquina, para alterar a porta basta passar a porta desejada como parâmetro 

~~~ Bash
python3 manage.py runserver [porta]
~~~

## Cadastrando Clientes

Para começar a sua lista de clientes basta digitar a url **/person/list/**

<p align="center"><img src="/imagens/person-list.png"></p>