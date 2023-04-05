ano = int(input('Digite o ano do seu nascimento: '))
idade = 2022 - ano
if idade <= 9:
    print('Voce esta classificado na categoria MIRIM!')
elif idade <= 14:
    print('Voce esta classificado na categoria INFANTIL!')
elif idade <= 19:
    print('Voce esta classificado na categoria JUNIOR!')
elif idade <= 20:
    print('Voce esta classificado na categoria SENIOR!')
else:
    print('Voce esta classificado na categoria MASTER!')