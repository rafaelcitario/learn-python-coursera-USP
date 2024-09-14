number = int(input("digite um número: "))


def isBuzz(number) -> str:
    if number % 5 == 0:
        return "Buzz"
    return number


print(isBuzz(number))
