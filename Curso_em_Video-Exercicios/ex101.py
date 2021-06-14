from datetime import date


def voto(idade):
    if idade < 18:
        frase = 'VOTO NEGADO'
    elif idade < 60:
        frase = 'VOTO OBRIGATÓRIO'
    else:
        frase = 'VOTO OPCIONAL'
    return frase


atual = date.today().year
print('-' * 40)
ano = int(input('Em que ano você nasceu? '))
idade = atual - ano
print(f'Com {idade} anos: {voto(idade)}.')