#Faça um programa que leia 5 números e informe o maior número.
num = [3, 6, 9, 2, 7]

print(max(num))

#Crie uma lista de locais que você gostaria de conhecer no mundo, 
#na ordem do local que você dá mais prioridade para o local que você dá menos prioridade. 
#Exiba a lista nas seguintes configurações: a) ordem original; b) ordem alfabética
#c) ordem de prioridades inversa; d) quantidade de itens
local = ['Tailândia', 'Portugal', 'Africa do Sul', 'Peru', 'Chile']

print('Ordem original: ', local)

print('Ordem alfabética: ', local.sort(), local)

print('Ordem de prioridades inversa: ', local.sort(reverse=True), local)

print('Quantidade de itens: ', len(local))

#Crie uma lista com os preços dos jogos que você mais gosta. a) Imprima o preço mais caro;
#b) Imprima o preço mais barato.
preco = [50.0, 45.5, 15.2, 90.8]

print('O preço mais caro é R$', max(preco))
print('O preço mais barato é R$', min(preco))

#Escreva um programa em Python que leia um vetor V1 de n posições e gere um vetor V2 de 
#tamanho n que é o vetor V1 invertido.
v1 = []
n = int(input('Indique a quantidades de posições: '))

for i in range(n):
  v1.append(input(f'Insira o {i+1}º elemento do seu vetor: '))

v2 = v1[::-1]

print(f'V1 = {v1} \n'
      f'V2 = {v2}')

#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
for n in range(1, 51):
  if n % 2 != 0:
    print(n)

#Faça um programa que recebe um número de 1 a 10 do usuário e imprime a tabuada 
#de multiplicação desse número
numero = int(input('Insira um número de 1 a 10: '))
tabuada = []

for i in range(10):
  tabuada.append(numero * (i+1))

# Imprimindo a tabuada
print(f"\n{'-'*30}"
      f"\n|{f'TABUADA DE {numero}':^28}|"
      f"\n{'='*30}")
for i in range(10):
  print(f"{f'{numero} x {i+1}': >14}"
        f" = "
        f"{f'{tabuada[i]}': <14}")
print(f"{'-'*30}")

#Faça um programa que recebe do usuário 10 valores de números inteiros, armazena 
#em um vetor e apos percorre-lo exibe qual é o maior valor e a sua posição.
vetor = []

for i in range(10):
  vetor.append(int(input(f'Insira o {i+1}º valor: ')))

print(f"\nO numero menor do vetor é {min(vetor)} na posicao {vetor.index(max(vetor))}"
      f"\nO numero maior do vetor é {max(vetor)} na posição {vetor.index(min(vetor))}")

#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor 
#seja inválido e continue pedindo até que o usuário informe um valor válido.
nota = int(input('Informe uma nota: '))

while (nota < 0) or (nota > 10):
   nota = int(input('Valor inválido!!!! \nInsira uma nota entre 0 e 10: '))

print("\nNota válida! Valor registrado!")

#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual 
#ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
nome = input('Insira seu nome: ')
senha = str(input('Insira uma senha: '))

while nome == senha:
  senha = str(input('Erro! Senha igual ao nome. Insira uma nova senha: '))

print('Senha válida!')

#Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos 
#números primos existentes entre 1 e um número inteiro informado pelo usuário.
n = int(input('Digite o valor máximo da lista de números primos: '))
primos = []

for i in range(1, n + 1):
  aux = 0
  for j in range(1, i):
    if i % j != 0:
      aux += 1
    if aux == i - 2 or i == 2:
      primos.append(i)

print(f"Números primos = {primos}")

#Faça um programa que calcule o mostre a média aritmética de N notas.
notas = [10, 8, 9, 2]

print(f'A média das notas {notas} é {sum(notas)/len(notas)}')
