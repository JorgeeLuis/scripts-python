qntd_vendas_coca= 150
qntd_vendas_pepsi= 130
preco_coca_und= 1.50
preco_pepsi_und= 1.50
custo_loja= 2.500

print('1. Qual foi o faturamento de Pepsi da Loja?')
faturamento_pepsi = (qntd_vendas_pepsi*preco_pepsi_und)
print('R= O faturamento de Pepsi foi R$ {}'.format(faturamento_pepsi))

print('2. Qual foi o faturamento de Coca da Loja?')
faturamneto_coca = (qntd_vendas_coca*preco_coca_und)
print('R= O faturamento de Coca-Cola foi R$ {}'.format(faturamneto_coca))

print('3. Qual foi o Lucro da loja?')
faturamento_total = (faturamento_pepsi+faturamneto_coca)
lucro = (faturamento_total-custo_loja)
print('Lucro da loja foi de R$ {}'.format(lucro))

print('4. Qual foi a Margem da Loja?')
margem_lucro = (lucro/faturamento_total)
print('A margem de lucro da loja foi R$ {}'.format(margem_lucro))
