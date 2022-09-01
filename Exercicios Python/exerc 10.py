

cigarros = float(input('Quantos cigarros por dia? '))
anos = float(input('Quantos anos? '))

cigarrost = cigarros * 365 * anos
tempom = cigarrost * 10
tempoh = tempom / 60
tempd = tempoh / 24
anospr = tempd / 365
print(f'dias perdidos {tempd:.0f} ou {anospr:.1f} ano(s).')
