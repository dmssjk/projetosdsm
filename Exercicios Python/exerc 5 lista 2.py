##5. Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = float(input('digite o primeiro n. '))
n2 = float(input('digite o segundo n. '))
n3 = float(input('digite o terceiro n. '))

valor = [n1,n2,n3]

maior = max (valor)
menor = min (valor)
print (f'o maior numero é {maior:.0f}, e o menor numero é {menor:.0f}')

