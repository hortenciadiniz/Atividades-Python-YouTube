#FACA UM PROGRAMA QUE LEIA UM ANO QUALQUER E FALE SE ELE EH OU NAO BISSEXTO
ano = int(input('Digite um ano para sabermos se eh ou nao um ano bissexto: '))
if ano%4 == 0:
    print('Esse eh ano um bissexto!')
else:
    print('Esse NAO eh um ano bissexto!')