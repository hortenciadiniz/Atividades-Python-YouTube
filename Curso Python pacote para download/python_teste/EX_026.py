#LEIA UMA FRASE PELO TECLADO E MOSTRE QUANTAS VEZES APARECE A LETRA A
#EM QUE POSICAO APARECE A PRIMEIRA VEZ
#EM QUE POSICAO APARECE A ULTIMA VEZ

frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase!'.format(frase.count('A')))
print('A primeira letra A apareceu na posicao {}'.format(frase.find('A')+1)) #+1 porque fica estranho mostrar posicao 0, caso o primeiro A esteja na primeira posicao
print('A ultima letra A apareceu na posicao {}'.format(frase.rfind('A')+1))