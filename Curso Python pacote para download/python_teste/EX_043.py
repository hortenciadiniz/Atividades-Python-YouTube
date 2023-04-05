#IMC

peso = float(input('Digite seu peso em kgs: '))
h = float(input('Digite sua altura em centimetros: '))
h_metros = h/100
imc = peso/(h_metros**2)

if imc < 18.5:
    print('Seu IMC eh {:.2f} e voce esta ABAIXO do peso'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC eh {:.2f} e voce esta com o peso IDEAL!'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC eh {:.2f} e voce esta com SOBREPESO! Se cuide!'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC eh {:.2f} e voce esta com OBESIDADE! Voce precisa fazer dieta e treinar!'.format(imc))
else:
    print('Seu IMC eh {:.2f} e voce esta com OBESIDADE MORBIDA! Essa condicao eh extremamente perigosa'.format(imc))