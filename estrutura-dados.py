import math

altura = 1.75
peso = 110

def showDataStruture(n1, n2):
  integer = 'número inteiro: ', n1 // n2
  floating = 'número flutuante: ', n1 / n2
  rest = 'resto da divisão: ', n1 % n2
  return [
     integer,
     floating,
     rest
  ]

def calculeImc(peso, altura):
  imc = peso // math.sqrt(altura)
  return imc

def imprimeAllCharacters(str):
  for char in range(len(str)):
    multiplicator = char + 1
    for space in range(len(str), 0, -1):
      space = space - multiplicator
      print(' ' * space, str[char] * multiplicator, str[char] * multiplicator, ' ' * (space - 1))
      break



imc = calculeImc(peso, altura)
print(imc)
print(showDataStruture(10, 3))
imprimeAllCharacters('schwarsenagger')
