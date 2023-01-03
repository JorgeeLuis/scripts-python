nome = input(print('Qual é o seu nome? '))
quantidade = input(print('qual é o valor adquerido? '))
meta = input(print('qual é o valor da meta? '))
if quantidade >= meta:
    print('Parabéns {}, você bateu a meta de {}'.format(nome,quantidade))
    print('Fim do programa!') 
else:
    print('{}, infelizmente não bateu a meta de {}'.format(nome,meta))
    print('Fim do programa!')
