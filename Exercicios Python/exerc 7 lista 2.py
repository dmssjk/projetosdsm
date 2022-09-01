##7. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
##ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
##em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
##compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.

area = float(input('metragem total? '))

rendimentometro = 1 / 3 
gastolitros = area * rendimentometro
numerolatas = gastolitros / 18
latas = (round(numerolatas))
custo = latas * 80

##print (f'Litros necessarios {gastolitros:.2f}, ou exatamente {numerolatas:.2f} latas, ou seja {latas:.0f} lata(s)')
print (f'total de latas {latas:.0f}, custo total R$ {custo:.2f}')




