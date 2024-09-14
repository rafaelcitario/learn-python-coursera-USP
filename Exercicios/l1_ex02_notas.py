notas = [
    float(input("digite a primeira nota: ")),
    float(input("digite a segunda nota: ")),
    float(input("digite a terceira nota: ")),
    float(input("digite a quarta nota: ")),
]


def arithmeticMean(arr):
    count = 0
    for note in arr:
        count += note
    return count / len(arr)


average = arithmeticMean(notas)
print("A média aritmética é %0.1f" % average)
