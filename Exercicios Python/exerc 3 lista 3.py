a = 80000
crescimentoaano =  3 * a / 100
b = 200000
crescimentobano =  1.5 * b / 100
crescimentox = a + crescimentobano
print(crescimentox)
while b >= a:
    a = crescimentox * crescimentobano


##print(f'aumento de {crescimentoaano:.0f} pessoas por ano ')
##print(f'aumento de {crescimentobano:.0f} pessoas por ano ')

## quero imprimir por ano o aumento populacional
## imprimir o numero de anos que demora para a igualar b
## crescimento composto
## ano 1 + crescimento x /// ano2  = (ano1 + crescimento) * crescimento x
## resposta 63 anos
