#LEIA A DISTANCIA DE UMA VIAGEM EM KM, CALCULE O PRECO DA PASSAGEM, R$0,50 POR KM PARA VIAGENS ATE 200KM E R$0,45 PARA >

distancia = float(input('Qual sera a distancia da sua viagem? '))
if distancia <= 200:
    preco1 = distancia*0.50
    print('O preco da sua passagem sera de {}'.format(preco1))
else:
    preco2 = distancia*0.45
    print('O preco da passagem sera de {}'.format(preco2))