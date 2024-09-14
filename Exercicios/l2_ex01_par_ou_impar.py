number = int(input("digite um número: "))


def isEvenOrOdd(number):
    if number % 2 != 0:
        return "ímpar"
    return "par"


evenOrOdd = isEvenOrOdd(number)
print(evenOrOdd)
