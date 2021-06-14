from time import sleep
from Mlib import formata, funcoes, arquivo

arq = 'bancodedados.txt'

if not arquivo.teste(arq):
    arquivo.criar(arq)

while True:
    funcoes.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoas', 'Sair do sistema'])
    x = funcoes.validacao()
    if x == 1:
        funcoes.banco(arq)
        continue
    elif x == 2:
        funcoes.cadastro(arq)
        continue
    elif x == 3:
        formata.text('Saindo do sistema...', fmt=True, c='vermelho')
        sleep(1.5)
        print(f'\033[36m{("ATÉ LOGO!"):^40}')
        break
    else:
        formata.cor('ERRO! Digite uma opção válida!', 'vermelho')
        sleep(1)


