# 090213422450
numbers = input("digite um número: ")


def isRepeatedNumbers(numbers):
    repeated = []
    for n in range(0, len(numbers)):
        if n + 1 >= len(numbers):
            break
        if numbers[n] == numbers[n + 1]:
            repeated.append({"número": numbers[n], "posição": n})
            repeated.append({"número": numbers[n + 1], "posição": n + 1})
            continue

    if len(repeated) > 0:
        # return "Repetidos: " + str(repeated) + "\n"
        return "sim"

    # return "Sem repetidos"
    return "não"


isRepeated = isRepeatedNumbers(numbers)
print(isRepeated)
