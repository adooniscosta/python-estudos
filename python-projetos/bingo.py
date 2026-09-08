import random
bingo = []
print('Projeto Bingo')
print('_____________')
rodar = input('Deseja seguir com o programa? s/n: ').lower()
if rodar == 'n' or rodar == 'nao':
    print('Você preferiu não seguir com o programa! Programa encerrado.')

while rodar == 's':
    numero = random.randint(1, 80)
    while numero in bingo:
        print('Esse numero já foi sorteado! Sorteando outro.')
        numero = random.randint(1, 80)

    bingo.append(numero)
    print(f'Numero sorteado: {numero}')
    continuar = input('Continuar? s/n: ').lower()

    if continuar == 'n' or rodar == 'nao':
        print('Programa encerrado!')
        print(f'Esses foram os numeros sorteados:\n{bingo}')
        break

