# Clientes Django

Esta é uma básica aplicação feita em django para cadastro de clientes, com ela você pode criar, editar e deletar clientes.

## Requisitos 

- Python 3.8.6
- Pip3
- Virtualenv 20.4.6
- Django 3.2.3
- Vscode


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

Para começar a sua lista de clientes, basta digitar a url **/person/new/** e preencher as informações pedidas no formulário

<p align="center"><img src="/projeto/imagens/person-new.png"></p>

Quando o cadastro for salva, você será direcionado para a url **person/list/** e verá se o cliente cadastrado foi adicionado a lista

<p align="center"><img src="/projeto/imagens/person-list.png"></p>

Você também verá que pode deletar o cliente criado, ao clicar no botão "deletar", vocẽ será direcionado para a url **person/delete/id** e poderá confirmar se quer mesmo deletar o cliente

<p align="center"><img src="/projeto/imagens/person-delete.png"></p>
