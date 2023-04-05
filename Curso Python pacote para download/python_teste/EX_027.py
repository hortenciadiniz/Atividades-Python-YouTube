#LEIA O NOME COMPLETO E MOSTRE APENAS O PRIMEIRO E O ULTIMO
name = str(input('Digite seu nome completo: ')).strip()
n = name.split() #slip divide a string grande em pedacos de strings
primeiro = n[0]
ultimo = n[len(n)-1]
print('Prazer em te conhecer {}, \nSeu primeiro nome eh {} \nSeu ultimo nome eh {}'.format(name, primeiro, ultimo))