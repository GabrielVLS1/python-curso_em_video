from lib.interface import *
from lib.arquivo import *

arq = 'pessoas.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq) 
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')