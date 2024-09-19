import math

numero = int(input("Digite um número inteiro: "))


def isCousin(number: int) -> str:
    for n in range(2, int(math.sqrt(number) + 1)):
        if number <= 1 or number % n == 0:
            return "não primo"
    return "primo"


NUMBER_IS_COUSIN: str = isCousin(numero)
print(f"%s" % NUMBER_IS_COUSIN)
