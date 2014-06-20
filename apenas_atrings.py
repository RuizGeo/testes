variavel = raw_input('Entre com o nome: ')

while variavel != 'sair':
    
    if str(variavel).isdigit():
        print 'Inserir apenas string'
        variavel = raw_input('Entre com o nome: ')
    else:
        variavel = raw_input('Entre com o nome: ')
