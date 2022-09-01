## considere a empresa de telefonia tchau. abaixo de 200 minutos a empresa cobra 0,20 por minuto entre 200 e 400 o preço é ,018 acima de a 400 minutos o preço



minutos = float(input('Quantos minutos? '))
if minutos <= 200:
    preço = 0.20
elif minutos <= 400:
     preço = 0.18
elif minutos <=800:
    preço = 0.15
else:
    preço = 0.08
    
resultado = (minutos * preço)
print (f'R${resultado:.2f}')


    
