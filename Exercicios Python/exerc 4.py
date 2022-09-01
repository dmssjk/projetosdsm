## faça um programa que calcule o aumento do salario pergunte o valor do salario e a porcentagem dp aumento

salario = float(input('Qual seu salário atual ? '))
aumento = float(input('Qual a % do aumento ? '))

aumen = salario * aumento / 100
resultado = (aumen + salario)

print (f'seu novo salário é: R$ {resultado:.2f} ')
                      
