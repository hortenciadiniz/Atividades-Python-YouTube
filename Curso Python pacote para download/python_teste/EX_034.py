#PERGUNTE O SALARIO DE UM FUNCIONARIO E CALCULE O VALOR DO AUMENTO
#ACIMA DE 1250, AUMENTO DE 10%
#INFERIORES OU IGUAIS, AUMENTO DE 15%

n = float(input('Digite o valor do seu salario: '))
print('Calculando seu aumento...')
if n > 1250:
    new_n = n*1.10
    aumento = new_n - n
    print('Seu aumento foi de {:.2f}, portanto, seu novo salario sera de {:.2f}'.format(aumento,new_n))
else:
    new_n = n*1.15
    aumento = new_n - n
    print('Seu aumento foi de {:.2f}, portanto, seu novo salario sera de {:.2f}'.format(aumento,new_n))