from random import randint
from time import sleep

itens = ('PEDRA','PAPEL','TESOURA')
computador = randint(0,2)
print('=-'*15)
print('''Escolha uma opcao para jogar:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('A opcao escolhida vai ser: '))
print('=-'*15)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-='*15)
print('Sua escolha foi {}'.format(itens[jogador]))
print('A escolha do computador foi {}'.format(itens[computador]))
print('PORTANTO...')

if computador == 0: #PEDRA
    if jogador == 0:
        print('A JOGADA EMPATOU!')
    elif jogador == 1:
        print('O JOGADOR VENCEU!')
    elif jogador ==2:
        print('O COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVALIDA!')

elif computador == 1: #PAPEL
    if jogador == 0:
        print('O COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('A JOGADA EMPATOU!')
    elif jogador == 2:
        print('O JOGADOR VENCEU!')
    else:
        print('JOGADA INVALIDA!')

elif computador == 2: #TESOURA
    if jogador == 0:
        print('O JOGADOR VENCEU!')
    elif jogador == 1:
        print('O COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('A JOGADA EMPATOU!')
    else:
        print('JOGADA INVALIDA!')