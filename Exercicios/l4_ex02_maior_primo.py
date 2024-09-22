import math


def verificaSePrimo(number: int) -> int:
    for i in range(2, int(math.sqrt(number) + 1)):
        if number <= 1 or number % i == 0:
            return None
    return number


def maior_primo(number: int) -> int:
    checkPrimoMaisProximo = verificaSePrimo(number)
    state = True
    while state != False:
        if type(checkPrimoMaisProximo) != type(None):
            state = False
            return checkPrimoMaisProximo
        number -= 1
        checkPrimoMaisProximo = verificaSePrimo(number)
    return checkPrimoMaisProximo
