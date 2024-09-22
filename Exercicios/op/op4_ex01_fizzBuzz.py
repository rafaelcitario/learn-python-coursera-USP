def fizzbuzz(number: int) -> str | int:
    fizz = number % 3 == 0
    buzz = number % 5 == 0
    fizzAndBuzz = number % 5 == 0 and number % 3 == 0
    match True:
        case True if fizzAndBuzz:
            return "FizzBuzz"
        case True if fizz:
            return "Fizz"
        case True if buzz:
            return "Buzz"
        case _:
            return number
