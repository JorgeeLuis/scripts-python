#mini sistema de estoque
print('                         SISTEMA DE ESTOQUE                      v1.0')
produto = input('nome do produto: ')
categoria = input('categoria do produto: ')
qtde_produtos = input('quantidade de produtos: ')

#categorias:
alimentos = 50
bebidas = 75
limpeza = 30

if produto and categoria and qtde_produtos:
    qtde_produtos = int(qtde_produtos)
    if categoria == 'bebidas':
        if qtde_produtos <= bebidas:
            print ('solicitar {}, á equipe de compras, temos apenas {} unidades em estoque. A quantidade minima é {}'.format(produto, qtde_produtos, bebidas))
    elif categoria == limpeza:
        if qtde_produtos <= limpeza:
            print ('solicitar {}, á equipe de compras, temos apenas {} unidades em estoque. A quantidade minima é {}'.format(produto, qtde_produtos, limpeza))
    elif categoria == alimentos:
        if qtde_produtos <= alimentos:
            print ('solicitar {}, á equipe de compras, temos apenas {} unidades em estoque. A quantidade minima é {}'.format(produto, qtde_produtos, alimentos))
else:
    print('preencha corretamente')        
    