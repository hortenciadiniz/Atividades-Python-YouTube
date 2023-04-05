import math
n = float(input('Digite um angulo qualquer: '))
s = math.sin(math.radians(n))
print('O SENO do angulo {} e igual a {}'.format(n,s))
c = math.cos(math.radians(n))
print('O COSSENO do angulo {} e igual a {}'.format(n, c))
t = s/c
print('A TANGENTE do angulo {} e igual {}'.format(n, t))