#LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMECA OU NAO COM O NOME 'SANTO'

city = str(input('Digite o nome de uma cidade: ')).strip().upper()
cidade = city.split()
primeiro = (cidade[0] == 'SANTO')
print('Eh {} que a cidade comeca com SANTO'.format(primeiro))