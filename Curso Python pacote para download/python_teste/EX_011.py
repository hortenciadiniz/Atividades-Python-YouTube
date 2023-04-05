l = float(input('Qual a largura da parede em metros? '))
h = float(input('Qual a altura da parede em metros? '))
a = l*h
v = a/2
print('A area da parede e {:.3f} metros quadrados e a quantidade de tinta necessaria para pintar ela e {:.3f} litros de tinta'.format(a,v))