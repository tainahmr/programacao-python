#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax² + bx + c. 
#O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário 
#nas seguintes situações: a - Se o usuário informar o valor de A igual a zero, a equação não é do 
#segundo grau e o programa não deve pedir os demais valores, sendo encerrado; b - Se o delta calculado
#for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa; c - Se o delta
#calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário; d - Se o delta 
#for positivo, a equação possui duas raiz reais; informe-as ao usuário;
import math
a = int(input('Informe o valor de a: '))

if a < 0:
  print('A equação não é de segundo grau.')

else:
  b = int(input('Informe o valor de b: '))
  c = int(input('Informe o valor de c: '))
  
delta = b**2-(4*a*c)

if delta < 0:
  print('A equação não possui raízes reais.')

elif delta == 0: 
  r = -b / (2*a)
  print(f'O delta = 0 possui uma raíz. A raíz de {a}x + {b}x + {c} é igual a {r}')

elif delta > 0:
  r1 = (-b + math.sqrt(delta) ) / (2*a)
  r2 = (-b - math.sqrt(delta) ) / (2*a)
  print(f'O delta maior que 0 possui duas raízes. As raízes de {a}x + {b}x + {c} é igual a {r1} e {r2}')
  
#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano 
#é ou não bissexto.
ano = int(input('insira o ano: '))

if (ano%400 == 0) or (ano%4 == 0 and ano%100 != 100):
    print(ano, 'é bissexto.') 

else:
  print(ano, 'não é bissexto.')
  
#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
data = input('Insira a data no formato dd/mm/aaaa: ')

try:
  dia, mes, ano = data.split('/')

except ValueError:
  data = input('A data precisa estar no formato: dd/mm/aaaa: ')

print(dia)
print(mes)
print(ano)  

#Faça um Programa que leia um número e exiba o dia correspondente da semana.
#(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
dia = int(input('Digite um número de 1 a 7 para exibir o dia da semana:'))

if dia == 1:
  print('O dia da semana é Domingo')

elif dia == 2:
  print('O dia da semana é Segunda')

elif dia == 3:
  print('O dia da semana é Terça')

elif dia == 4:
  print('O dia da semana é Quarta')

elif dia == 5:
  print('O dia da semana é Quinta')

elif dia == 6:
  print('O dia da semana é Sexta')

elif dia == 7:
  print('O dia da semana é Sabádo')

else:
  print('Valor inválido')

#Crie um programa para um circo, no qual dada a idade de uma pessoa, seja indicado o
#valor do ingresso segundo as regras: a) A entrada para qualquer pessoa com menos de 
#4 anos ou maior que 60 é gratuita; b) a entrada para qualquer pessoa com idade entre 
#4 e 18 custa 20 reais; c) a entrada para qualquer pessoa com 18 ou mais custa 30 reais;
#d) estudantes e professores pagam meia-entrada.
idade = int(input('Informe a idade: '))
meia = input('Digite S se professor ou estudante, caso não, digite N. ')

if 4 >= idade <= 60:
  valor = 'é gratuíto'

elif 4 < idade < 18:
  valor = 20.00

elif 18 >= idade < 60:
  valor = 30.00

if meia == 'S' and valor != 'é gratuíto':
  valor /= 2

print(f'A entrada será R${valor}') 

#imprimir uma mensagem informando se um aluno foi aprovado ou reprovado em uma disciplina 
#com base em sua nota final. A nota mínima necessária para aprovação é 5 .  
  

