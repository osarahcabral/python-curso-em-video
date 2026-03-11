#Desafio 004 
# Faça um programa que leia algo pelo teclado e mostra na tela o seu tipo primitivo e todas as informações possíveis sobre eles

n1 = input('Digite algo: ')
print('{}'.format(type(n1)))
print('Só tem espaço? {}'.format(n1.isspace()))
print('É numerico? {}'.format(n1.isnumeric()))
print('É do alfabeto? {}'.format(n1.isalpha()))
print('É alfanumérico? {}'.format(n1.isalnum()))
print('É maiúsculo? {}'.format(n1.isupper()))
print('É minusculo? {}'.format(n1.islower()))
print('Está capitalizada? {}'.format(n1.istitle()))
