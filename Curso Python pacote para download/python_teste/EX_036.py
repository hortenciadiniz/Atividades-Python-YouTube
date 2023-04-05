#aprovador de emprestimo bancario para a compra de uma casa

valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual seu salario mensal? '))
anos = int(input('Em quantos anos voce quer pagar a casa? '))

#calculo da prestacao mensal
mensalidade = valor/(anos*12)

if mensalidade <= 0.3* salario:
    print('Parabens, seu emprestimo foi LIBERADO e a mensalidade da sua casa sera de {:.2f}'.format(mensalidade))
else:
    print('Infelizmente seu emprestimo foi negado!')