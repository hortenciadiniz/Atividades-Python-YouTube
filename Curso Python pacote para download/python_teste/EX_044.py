#PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO, CONSIDERANDO SEU PRECO NORMAL E CONDICAO DE PAGAMENTO:
#A VISTA DINHEIRO/CHEQUE: 10% DE DESCONTO
#A VISTA NO CARTAO: 5% DE DESCONTO
#EM ATE 2X NO CARTAO: PRECO NORMAL
#3X OU MAIS NO CARTAO: 20% DE JUROS

valor = float(input('Digite o valor do produto: '))
print('''Qual sera a forma de pagamento?
[1] `A vista dinheiro/cheque (-10%)
[2] `A vista no cartao (-5%)
[3] Em ate 2x no cartao (preco normal)x
[4] Em 3x ou mais no cartao (+20%)''')
opcao = int(input('Digite qual opcao voce escolheu: '))

if opcao == 1:
    valor_final = valor*0.90
    print('O valor final da sua compra sera de {:.2f}'.format(valor_final))
elif opcao == 2:
    valor_final = valor*0.95
    print('O valor final da sua compra sera de {:.2f}'.format(valor_final))
elif opcao == 3:
    print('O valor final da sua compra sera de {:.2f}'.format(valor))
elif opcao == 4:
    valor_final = valor*1.2
    print('O valor final da sua compra sera de {:.2f}'.format(valor_final))
else:
    print('Nao existe essa opcao! Digite uma opcao valida!')