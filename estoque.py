import random
import json

class Estoque:
    def __init__(self):
        pass
    def create(self, dados):
        id = random.randint(111, 999)
        lista = []
        nome = input('digite o nome do produto: ')
        qualidade = input('digite a qualidade: ')
        valor = float(input('digite o valor do produto: '))
        data_validade = input('digite a data de validade: ')
        fabricante = input('digite o nome do fabricante: ')
        descricao = input('digite a descricao do produto: ')
        categoria = input('qual e a categoria do produto: ')
        dados['id'] = id
        dados['nome'] = nome
        dados['qualidade'] = qualidade
        dados['valor'] = valor
        dados['data_validade'] = data_validade
        dados['fabricante'] = fabricante
        dados['decricao'] = descricao
        dados['categoria'] = categoria
        print(id)
        return dados
    
    def deletar(self, lista):
        contagem = 0
        id = int(input('digite o id do produto para exclui-lo: '))
        for i in lista:
            if i['id'] == id:
                del i['id']
                del i['nome']
                del i['qualidade']
                del i['valor']
                del i['data_validade']
                del i['fabricante']
                del i['descricao']
        return lista
        
    def findAll(self, lista):
        opcao = int(input('\n1 - procurar por nome\n2 - procurar por fabricante\n'))
        if opcao == 1:
            nome = input('digite um nome para buscar todos equivalentes: ')
            for i in lista:
                if i['nome'] == nome:
                    dados = i
            return print(dados)
        if opcao == 2:
            fabricante = input('alterar para qual fabricante?: ')
            for i in lista:
                if i['fabricante'] == fabricante:
                    dados = i
            return print(dados)
                    
    def findOne(self, lista):
        busca = int(input('digite o id a ser procurado: '))
        for i in lista:
            if i['id'] == busca:
                print(i)
                
    def atualizar(self, lista):
        procurar = int(input('digite o id do qual deseja atualizar: '))
        for i in lista:
            if i['id'] == procurar:
                print('\n __________________________\n| 1 - nome                 |\n| 2 - qualidade            |\n| 3 - valor                |\n| 4 - data de validade     |\n| 5 - fabricante           |\n| 6 - descricao            |\n| 7 - categoria            |\n|__________________________|')
                opcao = int(input('digite a opcao desejada: '))
                if opcao == 1:
                    nome = input('digite o nome a ser atualizado: ')
                    i['nome'] = nome
                elif opcao == 2:
                    qualidade = input('digite a qualidade a ser atualizada: ')
                    i['qualidade'] = qualidade
                elif opcao == 3:
                    valor = float(input('deseja atualizar para qual valor?: '))
                    i['valor'] = valor
                elif opcao == 4:
                    data_validade = input('atualize a validade do produto: ')
                    i['data_validade'] = data_validade
                elif opcao == 5:
                    fabricante = input('alterar o nome do fabricante: ')
                    i['fabricante'] = fabricante
                elif opcao == 6:
                    descricao = input('digite a nova descricao do produto: ')
                    i['descricao'] = descricao
                elif opcao == 7:
                    categoria = input('digite a nova categoria do produto: ')
                    i['categoria'] = categoria
        return lista
    def visualizar(self, lista):
        for i in lista:
            print('ID: {}\nNOME: {}\nQUALIDADE: {}\nVALOR: {}\nDATA DE VALIDADE: {}\nFABRICANTE: {}\nDESCRICAO: {}\nCATEGORIA: {}\n\n'.format(i['id'],i['nome'],i['qualidade'],i['valor'],i['data_validade'],i['fabricante'],i['descricao'],i['categoria']))
def main():
    lista = []
    while True:
        try:
            dados = {'id':'','nome':'','qualidade':'','valor':'','data_validade':'','fabricante':'','descricao':'','categoria':[]}
            print('\n                <controle de estoque>                  \n _____________________________________________________\n| 1 - criar novo produto                              |\n| 2 - deletar produto                                 |\n| 3 - procurar todos de um determinado nome/categoria |\n| 4 - procurar por apenas um produto                  |\n| 5 - atualizar produto                               |\n| 6 - visualizar todos itens                          |\n|_____________________________________________________|\n')
            opcao = int(input('digite sua opcao: '))
            a = Estoque()
            if opcao == 1:
                b = a.create(dados)
                lista.append(b)
            elif opcao == 2:
                c = a.deletar(lista)
                print(c)
            elif opcao == 3:
                d = a.findAll(lista)
            elif opcao == 4:
                e = a.findOne(lista)
            elif opcao == 5:
                f = a.atualizar(lista)
            elif opcao == 6:
                f = a.visualizar(lista)
        except Exception as e:
            pass
        


if __name__=="__main__":
    main()