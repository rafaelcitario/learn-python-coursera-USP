numero = int(input("Digite o valor de n: "))


def imprimeFatorialDoNatural(numero: int):
    fatorial = numero
    if numero > 0:
        for n in range(numero, 1, -1):
            fatorial *= n - 1
        return fatorial
    fatorial = 1
    return fatorial


fatorial = imprimeFatorialDoNatural(numero)
print(fatorial)
