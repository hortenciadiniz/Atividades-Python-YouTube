#LER A VELOCIDADE DE UM CARRO E DIZER SE ELE FOI OU NAO MULTADO

vel = float(input('Qual a velocidade do carro? '))
multa = (vel - 80)*7
if vel > 80:
    print('Voce foi multado por ultrapassar o limite de velocidade, sua multa custara {}'.format(multa))
else:
    print('Voce nao foi multado')