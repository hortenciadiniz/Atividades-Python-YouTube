#LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM SILVA NO NOME

name = str(input('Digite o nome de uma pessoa: ')).strip().upper()
teste = 'SILVA' in name
print('Analisando seu nome... \nEh {} que ele tem a palavra Silva'.format(teste))