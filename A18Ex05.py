from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 30)
print(' ' * 5, 'JOGOS NA MEGA SENA', ' ' * 5)
print('-' * 30)
qtos = int(input('Quantos jogos você quer sortear? '))
total = 1
while total <= qtos:
    cont = 0
    while True:
        numeros = randint(1, 60)
        if numeros not in lista:
            lista.append(numeros)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('--' * 6, f' SORTEIO DE {qtos} JOGOS ', '--' * 6)
for i, l in enumerate(jogos):
    print(f'Jogos {i+1}: {l}')
    sleep(1)
print('--' * 5, ' BOA SORTE TIME! ', '--' * 5)
