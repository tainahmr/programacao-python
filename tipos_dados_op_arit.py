#1 - Faça um Programa que mostre a mensagem "hello world!" na tela
print("hello world!")

#2 - Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
num = input('Insira um número: ')
print('O número informado foi', num)

#3 - Faça um Programa que peça dois números e imprima a soma.
num = int(input('Insira um número: '))
num2 = int(input('Insira outro número: '))

print('a soma é', num + num2)

#4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.
notas = float(input('Insira a primeira nota: '))
notas1 = float(input('Insira a segunda nota: '))
notas2 = float(input('Insira a terceira nota: '))
notas3 = float(input('Insira a quarta nota: '))

print('A média das notas é:', (notas + notas1 + notas2 + notas3) / 4)

#5 - Faça um Programa que converta metros para centímetros.
metro = float(input('Informe a medida em metros: '))

print(metro,' metro corresponde a', metro*100,'cm')

#6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
raio = float(input('Informe o raio de um círculo: '))

print('A área de um círculo de raio', raio, 'é: ', 3.14*raio**2)

#7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o 
# dobro desta área para o usuário.
area_quad = int(input('Informe o lado do quadrado: '))**2

print('A área do quadrado é: ', area_quad, 'e o dobro da área do quadrado é:', area_quad*2)

#8 - Faça um Programa que pergunte quanto você ganha por hora e o número de 
#horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
valor_hora = float(input('Informe o valor da hora: R$ '))
hora_mes = int(input('Informe as horas trabalhadas no mês: '))

print('O salário mês é R$', valor_hora*hora_mes)

#9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme 
#e mostre a temperatura em graus Celsius.
temp_f = float(input('Informe a temperatura em graus Fahrenheit: '))

print('A temperatura em graus Celsius é', 5*((temp_f - 32)/9))

#10 - Faça um programa que peça a temperatura em graus Celsius, transforme 
#e mostre em graus Fahrenheit.
temp_c = float(input('Informe a temperatura em graus Celsius: '))

print('A temperatura em graus Fahrenheit é', (temp_c*9/5)+32)

#11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo.
#soma do triplo do primeiro com o terceiro.
#terceiro elevado ao cubo.
num = int(input('Informe um número inteiro: '))
num2 = int(input('Informe outro número inteiro: '))
num3 = float(input('Informe um número real: '))

print('O produto do dobro do primeiro com metade do segundo é', num*2*num2/2)
print('A soma do triplo do primeiro com o terceiro é', num*3+num3)
print('O terceiro elevado ao cubo', num3**3)

#12 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que 
#calcule seu peso ideal, usando a seguinte fórmula: peso_ideal=(72.7×altura)−58
altura = float(input('Informe a altura: '))

print('Para altura de', altura,'m o peso ideal é', (72.7*altura)-58,'Kg.')

#13- Tendo como dado de entrada a altura ( h ) de uma pessoa, construa um 
# algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens:  (72.7×h)−58    Para mulheres:  (62.1×h)−44.7
h_h = float(input('Informe a altura do Homem: '))
h_m = float(input('Informe a altura da Mulher: '))

print('Para altura homem de', h_h, 'm o peso ideal é', (72.7*h_h)-58, 'Kg')
print('Para altura Mulher de', h_m, 'm o peso ideal é', (62.1*h_m)-44.7, 'Kg')

#14- João Papo-de-Pescador, homem de bem, comprou um microcomputador para 
#controlar o rendimento diário de seu trabalho. Toda vez que ele traz um 
#peso de peixes maior que o estabelecido pelo regulamento de pesca do 
#estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo
#excedente. João precisa que você faça um programa que leia a variável peso
#peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade
#de quilos além do limite e na variável multa o valor da multa que João deverá
#pagar. Imprima os dados do programa com as mensagens adequadas.
peso = float(input('Informe o peso de peixes em Kg: '))

if peso > 50:
  excedente = peso - 50
  multa = excedente*4.00
  print('O peso de peixes pescado é', peso,'Kg. O excedente de peso foi de', excedente,'Kg. A multa será de R$', multa)

else:
  print('O peso de peixes pescado é', peso,'Kg. Não houve excedente.')

#Faça um Programa que pergunte quanto você ganha por hora e o número de horas 
#trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
#sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 
#5% para o sindicato, faça um programa que nos dê:
#salário bruto / quanto pagou ao INSS / quanto pagou ao sindicato /
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
valor_hora = float(input('Informe qual o valor da hora trabalhada: '))
hora_trabalhada = int(input('Informe o número de horas trabalhadas no mês: '))
salario_bruto = valor_hora*hora_trabalhada
ir = salario_bruto*0.11
inss = salario_bruto*0.08
sind = salario_bruto*0.05
salario_liq = salario_bruto - ir  - inss - sind

print('O salário bruto é R$', salario_bruto, ',foi pago de INSS R$', inss, ', foi pago ao Sindicato R$', sind,'. Com os descontos, o salário liquido é de R$', salario_liq)

