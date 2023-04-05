#JOGUINHO:
import random
num = int(input('Estou pensando em um numero de 0 a 5, advinha qual eh? '))
num_sorteado_pelo_pc = random.randint(0,5)
if num == num_sorteado_pelo_pc:
    print('Voce acertou o numero que eu pensei! PARABENS!')
else:
    print('Infelizmente eu nao pensei nesse numero.\nSorry, eu pensei no numero {}'.format(num_sorteado_pelo_pc))