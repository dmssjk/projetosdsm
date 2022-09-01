##Determine se um ano é bissexto. Verifique no Google como fazer isso...



from calendar import isleap

ano = float(input('Digite o ano? '))

if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print('é bissexto')

else:
    print('não é bissexto')




       
