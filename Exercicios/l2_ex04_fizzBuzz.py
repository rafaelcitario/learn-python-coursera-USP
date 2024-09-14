number = int(input("digite um número: "))


def isFizzBuzz(number) -> str:
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    return number


print(isFizzBuzz(number))
