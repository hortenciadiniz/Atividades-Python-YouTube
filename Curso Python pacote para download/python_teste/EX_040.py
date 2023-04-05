#LEIA DUAS NOTAS E CALCULE SUA MEDIA
#ABAIXO DE 5.0: REPROVADO
#ENTRE 5.0 E 6.9: RECUPERACAO
#ACIMA DE 7.0 OU IGUAL: APROVADO

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
if m<5:
    print('Sua media foi {}, portanto voce esta REPROVADO!'.format(m))
elif 5<=m<7:
    print('Sua media foi {}, portanto voce esta em RECUPERACAO!'.format(m))
elif 7<=m<=10:
    print('Sua media foi {}, portanto voce esta APROVADO!'.format(m))
else:
    print('A media maxima eh 10, reveja se voce escreveu as notas separadamente dentro da faixa permitida, ou seja, entre 0 e 10!')