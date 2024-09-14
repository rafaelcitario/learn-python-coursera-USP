def getDozens():
    numeroStr = input("Digite um número inteiro: ")
    numbers = []

    for number in numeroStr:
        numbers.append(int(number))

    if len(numbers) <= 1:
        return int(0)
    return numbers[len(numbers) - 2]


dozens = getDozens()
print("O dígito das dezenas é %d" % dozens)
