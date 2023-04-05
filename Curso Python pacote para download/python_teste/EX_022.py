#PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
#NOME COM TODAS AS LETRAS MAIUSCULAS
#NOME COM TODAS AS LETRAS MINUSCULAS
#QUANTAS LETRAS TEM O NOME COMPLETO SEM CONSIDERAR OS ESPACOS ENTRE OS NOMES
#QUAL EH SEU PRIMEIRO NOME
#QUANTAS LETRAS TEM O PRIMEIRO NOME

nome = str(input('Digite seu nome completo: ')).strip() #strip ja vai eliminar os espacos antes e depois do nome completo
print('Analisando seu nome...')
maiusculo = nome.upper()
print('Seu nome com todas as letras maiusculas sera: {}'.format(maiusculo))

minusculo = nome.lower()
print('Seu nome com todas as letras minusculas sera: {}'.format(minusculo))

tamanho = len(nome)
qt_espacos = nome.count(' ')
print('A quantidade total de letras do seu nome, exceto os espacos, eh de {} letras'.format(tamanho - qt_espacos))

primeiro_espc = nome.find(' ')
primeiro_nome = nome[:primeiro_espc]
print('Seu primeiro nome eh: {}'.format(primeiro_nome))

qt_letras_nome = len(primeiro_nome)
print('Seu primeiro nome tem {} letras'.format(qt_letras_nome))

#outra forma de fazer eh separando o nome em split
#separa = nome.split()
#print('Seu primeiro nome eh {} e ele tem {} letras'.format(separa[0], len(separa[0])))