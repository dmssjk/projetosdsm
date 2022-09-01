##a. + Salário Bruto : R$
##b. - IR (11%) : R$
##c. - INSS (8%) : R$
##d. - Sindicato ( 5%) : R$
##e. = Salário Liquido : R$

ghora = float(input('valor hora? '))
qhora = float(input('horas trabalhadas? '))
sbruto =  (ghora * qhora)
ir = 11
inss = 8
sind = 5
irtotal = sbruto * ir / 100
insstotal = sbruto * inss / 100
sindtotal = sbruto * sind / 100
sliquido =  sbruto - irtotal - sindtotal - insstotal

print(f' salario bruto: R$ {sbruto:.2f}')

print(f'  Descontos')
print(f'   imposto de renda:  - R$ {irtotal:.2f}')
print(f'   inss: - R$ {insstotal:.2f}')
print(f'   sindicato: - R$ {sindtotal:.2f}')

print(f' salario liquido: R$ {sliquido:.2f}')


##print(f'salario bruto R$ {sbruto:.2f}')
##print(f'imposto de renda R$ {irtotal.0f}')
