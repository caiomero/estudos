#Ex03. Faça um programa que peça o nome, 3 notas de um aluno, e armazene-os em um dicionário, também armazene nesse dicionário a média e a situação do aluno (>= 6 está aprovado, se não reprovado.
aluno = {}

aluno ['nome'] = input('digite o seu nome: ')
aluno ['nota1'] = int(input('digite a primeira nota:'))
aluno ['nota2'] = input('digite a segunta nota: ')
aluno ['nota3'] = input('digite a terceira nota: ')
aluno ['media'] = (aluno.get('nota1') + aluno.get('nota2') + aluno.get('nota3') )/ 3
