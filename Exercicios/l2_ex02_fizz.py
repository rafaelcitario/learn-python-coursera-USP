number = int(input("digite um número: "))


def primeFizz(number) -> str:
    if number % 3 == 0:
        return "Fizz"
    return number


print(primeFizz(number))
