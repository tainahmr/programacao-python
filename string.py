#Faça um programa que leia uma string e a imprima.
frase = input('Insira uma frase: ')

print(frase)

#Crie um programa que imprima o comprimento de uma string.
palavra = 'python'

print(len(palavra))

#Crie um programa que compara duas strings.
palavra = 'python'

print('é igual') if palavra == 'python' else print('Não é igual')

#Faça um programa que leia um nome e imprima as 4 primeiras letras do nome.
nome = input('informe um nome: ')

print(nome[:4])

#Escreva um programa que substitui as ocorrencias de um caractere 0 em uma string por outro caractere 1.
num = '010101'

print(num.replace('0', '1'))

#Entre com um nome e imprima o nome somente se a primeira letra do nome for “a”.
nome = input('Escreva um nome: ')

if nome[0].lower() == 'a':
  print(nome)

else:
    print('Insira o nome novamente.')

#Faça um programa que receba do usuario uma string. O programa imprime a string sem suas vogais.
string = input('Insira seu nome: ')

for vogal in 'aeiouAEIOU':
  string = string.replace(vogal, '')

print('String sem vogais: ', string)

#Faça um programa em que troque todas as ocorrencias de uma letra L1 pela letra L2 em uma string. 
#A string e as letras L1 e L2 devem ser fornecidas pelo usuario.
string = input('Insira uma frase: ')
l1 = input('Insira o caractere a ser substituído: ')
l2 = input('Insira o caractere novo: ')

print(string.replace(l1,l2))

#Faça um programa para converter uma letra maiuscula em letra minuscula. 
#Use a tabela ASCII para resolver o problema.
letra = input('Informe uma letra maiuscula: ')

if 64 < ord(letra) < 91:
  letra = chr(ord(letra) + 32)

print(letra)

#Ler nome, sexo e idade. Se sexo for feminino e idade menor que 25, imprime o nome da 
#pessoa e a palavra “ACEITA”, caso contrario imprimir “NÃO ACEITA”.
nome = input('Insira o seu nome: ')
sexo = input('Insira F se seu sexo for feminino e M se for masculino: ')
idade = int(input('Insira sua idade: '))

if sexo == 'F' and idade < 25:
  print('Aceita')

else:
  print('Não aceita!')

#Faça um programa que conte o numero de 1's que aparecem em um string. Exemplo: 0011001 -> 3
string = '0011001'

print(string.count('1'))

#Faça um programa que receba uma palavra e a imprima de tras-para-frente.
string = input('insira uma palavra: ')

print(string[::-1])

#Faça um programa que receba uma palavra e calcule quantas vogais (a, e, i, o, u) possui essa palavra. 
#Entre com um caractere (vogal ou consoante) e substitua todas as vogais da palavra dada por esse caractere.
palavra = input('Insira uma palavra: ')
caractere = input('Insira o caractere que irá substituir a vogal: ')

qtd_a = palavra.lower().count('a')
qtd_e = palavra.lower().count('e')
qtd_i = palavra.lower().count('i')
qtd_o = palavra.lower().count('o')
qtd_u = palavra.lower().count('u')

print(f"\n{'Contagem de vogais':^30}"
      f"\na: {qtd_a}"
      f"\ne: {qtd_e}"
      f"\ni: {qtd_i}"
      f"\no: {qtd_o}"
      f"\nu: {qtd_u}")

print('Nova palavra: ', palavra.replace('a', caractere).replace('e', caractere).replace('i', caractere).replace('o', caractere).replace('u', caractere))

#Ler uma frase e contar quantos caracteres sao brancos. 
#Lembre-se que uma frase e um conjunto de caracteres (vetor).
frase = input('Escreva uma frase: ')

print(frase.count(' '))

#Faça um programa que leia uma palavra e some 1 no valor ASCII de cada 
#caractere da palavra. Imprima a string resultante.
palavra = input('Insira uma palavra: ')
palavra_final = []

for caractere in palavra:
  palavra_final.append(chr(ord(caractere) + 1))

print(palavra_final)

#Leia uma cadeia de caracteres e converta todos os caracteres para maiuscula. 
#Dica: subtraia 32 dos caracteres cujo codigo ASCII esta entre 65 e 90.
cadeia = input('Insira uma cadeia de caracteres: ')

for caractere in cadeia:
  if 96 < ord(caractere) < 123:
    print(chr(ord(caractere) - 32), end='')

  else:
    print(caractere, end='')
    
#Escreva um programa para converter uma cadeia de caracteres de letras maiusculas em letras minusculas.
cadeia = input('Insira uma cadeia: ')

for caractere in cadeia:
  if 64 < ord(caractere) < 91:
    print(chr(ord(caractere) + 32), end='')

  else:
    print(caractere, end='')

#Leia um vetor contendo letras de uma frase inclusive os espaços em branco. 
#Retirar os espaços em branco do vetor e depois escrever o vetor resultante.
frase = input('Insira uma frase: ')

print(frase.replace(' ', ''))

#

