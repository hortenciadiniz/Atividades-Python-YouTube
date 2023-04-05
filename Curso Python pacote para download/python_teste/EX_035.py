#LEIA 3 SEGMENTOS DE RETAS E DIGA SE ELES PODEM OU NAO FORMAR UM TRIANGULO

a = float(input('Primeiro segmento de reta: '))
b = float(input('Segundo segmento de reta: '))
c = float(input('Terceiro segmento de reta: '))
print('='*20)
print('Analisando se esses tres segmentos formam um triangulo...')
print('='*20)
#testar pra saber qual o menor lado
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#teste pra saber qual eh o valor do meio, ou seja, o segundo menor
meio = a
if a<b<c:
    meio = b
if a<c<b:
    meio = c
#teste para saber qual o maior lado
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
#teste para ver se a soma dos dois menores eh maior que o terceiro lado
if menor == meio or menor == maior or maior==meio:
    print('Esses segmentos de reta serao SIM capazes de formar um triangulo e ele sera chamado de ISOSCELES!')
if menor+meio>maior:
    print('Esses segmentos de reta sao SIM capazes de formar um triangulo e ele sera chamado de ESCALENO!!')
if menor == meio == maior:
    print('Esses segmentos de reta serao SIM capazes de formar um triangulo e ele sera chamado de EQUILATERO!')
else:
    print('Esses segmentos de reta NAO sao capazes de formar um triangulo!')