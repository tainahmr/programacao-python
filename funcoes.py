#Crie um programa que receba um valor inteiro e avalie se ele é positivo ou negativo. 
#Essa avaliação deve ocorrer dentro de uma função que retorna um valor booleano.
def positivo(n):
  return n >= 0


numero = int(input('Insira um número inteiro: '))
print(f"\nO número {numero} é:")
print("POSITIVO") if positivo(numero) else print("NEGATIVO")

#Crie um programa que tenha uma função que receba uma lista de números inteiros e exiba 
#todos os valores multiplicados por um valor inserido pelo usuário.
def multi(lista, n):
  for num in lista:
    print(f"{n:3} x {num:3} = {n * num}")

lista = []
n = int(input('Insira o valor que você quer multiplicar pela lista: '))

len_lista = int(input('Insira a quantidade de valores que você quer multiplicar: '))
for i in range(len_lista):
  lista.append(int(input(f"Insira o {i + 1}º valor: ")))

print('\nMULTIPLICAÇÕES')
multi(lista, n)

#Crie um programa que possua uma lista de nomes. Peça que o usuário insira um nome 
#que será buscado nesta lista. A busca deve ser implementada em uma função que retorna 
#os valores lógicos verdadeiro ou falso.
def busca_nome(lista_nomes, nome_buscado):
  for nome in lista_nomes:
    if nome.lower() == nome_buscado.lower():
      return True
    return False

lista = ['Maria', 'José', 'Antonia', 'Mario', 'Carlos']

nome_buscado = input('Insira o nome a ser buscado: ')

if busca_nome(lista, nome_buscado):
  print(f'{nome_buscado.capitalize()} aparece na lista na posição {lista.index(nome_buscado.capitalize())}')

else:
  print('Não existe esse nome na lista!')
  
#Implemente um programa que possa receber do usuário a temperatura em graus Celsius ou Fahrenheit. 
#Antes de receber a temperatura, pergunte ao usuário se ele deseja inserir em Celsius ou em Fahrenheit. 
#Se a entrada for em graus Celsius, o programa deverá retornar a temperatura em Fahrenheit. 
#Se a entrada for em Fahrenheit, o programa deverá retornar a temperatura em Celsius.
def conversor_f(c):
  f = c*1.8+32
  return f

def conversor_c(f):
  c = (f-32)/1.8
  return c

temp = float(input('Insira a temperatura: '))
medida = input('Insira C se graus Celsius ou F se Fahrenheit: ')

print('\nCONVERSOR TEMPERATURA ')
if medida == 'F':
  print(f"{temp}ºC = {conversor_f(temp)}ºF")

elif medida == 'C':
  print(f"{temp}ºF = {conversor_c(temp)}ºC")

else:
  print(f"Medida Inválida!")
  
#Crie um programa que receba do usuário 5 números inteiros e os exiba na tela na ordem contrária 
#a que foi inserido. A leitura dos números deve ser feita em uma função e a exibição dos valores 
#em ordem contrária deve ocorrer em outra função.
def recebe_lista():
  lista = []
  for i in range(5):
    lista.append(int(input(f"Digite o {i+1}º valor inteiro: ")))
  return lista

def inverter(lista):
  for numero in lista[::-1]:
    print(numero)

lista = recebe_lista()
print(inverter(lista))

#Faça um programa para imprimir:
#1
#2   2
#3   3   3
#.....
def escadinha(n):
  print('\n')
  for caractere in range(1, n + 1):
    linha = ''
    for _ in range(0, caractere):
      linha += f'{caractere} '
    print(linha)

escadinha(int(input('Insira seu número: ')))

#Faça um programa para imprimir:
#1
#1   2
#1   2   3
def escadinha_coluna(n):
  print('\n')
  for caractere in range(1, n + 1):
    linha = ''
    for i in range(0, caractere):
      linha += f'{i + 1}\t'
    print(linha)

escadinha_coluna(int(input('Insira seu número: ')))

#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: 
#taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo 
#de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.
def soma_imposto(taxa_imposto, custo):
  return custo * ((taxa_imposto/100)+1)

taxa_imposto = float(input('Taxa imposto: '))
custo = float(input('Custo: '))
custo = soma_imposto(taxa_imposto, custo)

print(f"\nO custo com a taxa de imposto é R$ {custo:.2f}")

#Um palíndromo é uma palavra que se soletra da mesma forma nos dois sentidos, como “osso” e “reviver”. 
#Escreva um função que dado uma plavra verifique se ela é palindro.
def verifica_palindromo(palavra):
  return palavra.lower()  == palavra[::-1].lower()

palavra = input('Insira uma palavra: ')
print(f"{palavra.capitalize()} é um palíndromo") if verifica_palindromo(palavra) else print(f"{palavra.capitalize()} Não é um palindromo!")

#Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. 
#Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação 
#possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta 
#ou caixa baixa, independentemente de como foram digitados.
import random

def embaralha(string):
  string_embaralhada = random.sample(string,len(string))
  return ''.join(string_embaralhada)

texto = input('Insira uma string: ')
print(embaralha(texto))

