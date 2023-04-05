n1 = int(input('Um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1+n2
m = n1* n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma vale {}'.format(s), end=' ') #esse end serve pra juntar a linha debaixo com essa linha
print('A multiplicacao vale {}'.format(m))
print('A divisao vale {:.3f}'.format(d)) #divisao com 3 casas decimais flutuante
print('A divisao inteira vale {}'.format(di))
print('A potencia \n vale {}'.format(e)) #\n serve pra pular linha