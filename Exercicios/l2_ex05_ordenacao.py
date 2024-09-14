numbers = []
for index in range(0, 3):
    numbers.append(int(input("digite um número: ")))
    if index == 3:
        break


def isSorted(numbers):
    for index in range(len(numbers) - 1):
        if index + 1 > len(numbers):
            return True

        if numbers[index] <= numbers[index + 1]:
            continue
        return False


isSorted = isSorted(numbers)
message = "crescente" if isSorted != False else "não está em ordem crescente"
print(message)
