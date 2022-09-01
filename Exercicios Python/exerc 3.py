dias = float (input('Quantos dias? '))
horas = float (input('Quantas horas? '))
minutos = float (input('Quantos minutos? '))
segundos = float (input('Quantos segundos? '))
resultadod = dias * 24 * 60 * 60
resultadoh = horas * 60 * 60
resultadom = minutos * 60

print (resultadod + resultadoh + resultadom + segundos)


## um dia tem 24*60*60
## total = d*24*60*60 + h*60*60 + m*60 + s

