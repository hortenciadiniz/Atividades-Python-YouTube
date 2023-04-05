#faca um programa que leia 3 numeros e mostre qual eh o maior e qual eh o menor

a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))
#primeiro testar para o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

#depois testar para o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
#exibir na tela qual o maior e qual o menor no mesmo print
print('O menor valor digitado foi: {}\nO maior valor digitado foi {}'.format(menor,maior))