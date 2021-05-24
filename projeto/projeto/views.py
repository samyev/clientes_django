from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    # função que retorna um 'olá mundo! importado de index.html'
    return render(request, 'index.html')

def articles(request, year):
    # função que retorna o ano que o usuário informar na url
    return HttpResponse("O ano informado foi: " + str(year))


def lerDoBanco(nome):
    # Função que procura o nome solicitado pelo usuário dentro do "banco" lista_nomes
    returned_pessoa = {'Nome': 'N encontrado', 'idade': 0}
    lista_nomes = [
        {'nome': 'Ana', 'idade': 20},
        {'nome': 'Pedro', 'idade': 25},
        {'nome': 'Joaquim', 'idade': 27},
    ]

    for pessoa in lista_nomes:
        if nome in pessoa.values():
            returned_pessoa = pessoa

    return returned_pessoa


def fname(nome):
    # essa função retorna o nome da pessoa solicitada direto do banco e moatra na tela do site
    result = lerDoBanco(nome)
    if result['idade'] != 0:
        return print('A pessoa foi encontrada, ela tem ' + str(result['idade']) + ' anos')
    else:
        return print('A pessoa não foi encontrada')

def fname2(request, nome):
    idade = lerDoBanco(nome)['idade']
    return render(request, 'pessoa.html', {'v_idade': idade})
