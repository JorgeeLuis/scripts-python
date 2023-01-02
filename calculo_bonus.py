print('CALCULADORA BÔNUS')

funcionario01 = input ('DIGITE SEU NOME: ')

vlr_vnds01 = (int(input('DIGITE O VALOR DE VENDAS ')))

meta01 = 1000
meta02 = 2000

if funcionario01 == '' or vlr_vnds01 == '':
    print('Inválido! Preencha corretamente!')
elif vlr_vnds01 >= meta01:
    bonus = vlr_vnds01 * 0.1 
elif vlr_vnds01 >= meta02:
    bonus = vlr_vnds01 * 0.15
else:
    bonus = 0
print('O bônus de {} é {}'.format(funcionario01,bonus))
