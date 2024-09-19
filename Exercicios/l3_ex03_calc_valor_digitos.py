numero = input("Digite um número inteiro: ")


def calcValorDigitos(numero: str) -> int:
    total = 0
    for i in range(0, len(numero)):
        total += int(numero[i])
    return total


calcDigitos = calcValorDigitos(numero)
print(calcDigitos)
