import random

print('bem vindo ao gerador de senha')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%¨&*().,?0123456789'

number = input('Quantidade de senhas a gerar: ')
number = int(number)

Tamanho = input('tamanho da sua senha: ')
Tamanho = int(Tamanho)

print('\nEssa é sua senha: ')

for pwd in range(number):
    senhas = ''
    for c in range(Tamanho):
        senhas += random.choice(chars)
    print(senhas)