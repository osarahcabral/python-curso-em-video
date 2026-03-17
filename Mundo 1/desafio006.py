#Desafio 006 
#Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada

n = int(input('Digite um valor: '))
print('O dobro é {}, o triplo é {} e sua raiz quadrada é {}'.format(n*2, n*3, pow(n,1/2)))
