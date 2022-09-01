user = str(input('crie um novo usuario: '))
senha = str(input('crie uma senha (não pode ser igual ao usuario):'))
while senha == user:
    senha = input('tente novamente, digite uma nova senha: ')
else:
    print ('novo usuario criado com sucesso')

##print (user)
##print (senha)
