#Ex02. Faça um programa que peça o nome, raça e cor de um animal e armazene as informações em um dicionário. Ao final mostre os valores nas chaves do dicionário.
animais = {}

animais ['nome'] = input('Qual é o nome do seu animal: ')
animais ['raca'] = input('Qual é a raça do seu animal: ')
animais ['cor'] = input('Qual é a cor do seu animal: ')

print ('dados do animal:')
print (f'-nome {animais.get('nome')}')
print (f'-raça {animais.get('raca')}')
print (f'-cor {animais.get('cor')}')