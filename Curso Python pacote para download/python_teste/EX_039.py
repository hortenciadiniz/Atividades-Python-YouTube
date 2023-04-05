#LEIA O ANO DE NASCIMENTO E INFORME DE ACORDO COM SUA IDADE
#SE ELE AINDA VAI SE ALISTAR AO SERVICO MILITAR, LEMBRANDO QUE A IDADE EH DE 18 ANOS
#SE EH A HORA DE SE ALISTAR
#SE JA PASSOU DO TEMPO DE ALISTAMENTO
#TBM DEVE MOSTRAR QUANTO TEMPO FALTA OU HA QUANTO TEMPO PASSOU DO PRAZO

ano = int(input('Em qual ano voce nasceu? '))
idade = 2022 - ano
falta = 18 - idade
passou = idade - 18
if idade < 18:
    print('Falta(m) {} anos para voce se alistar no servico militar!'.format(falta))
elif idade == 18:
    print('Esta na hora de voce se alistar, pois voce tem 18 anos!')
else:
    print('O tempo de voce se alistar no servico militar ja passou {} anos'.format(passou))

