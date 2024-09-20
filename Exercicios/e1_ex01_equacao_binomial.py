# (n k) = n! / k! * (n-k)!


def fatorial(number: int, *args: int) -> int:
    coefs = 1
    for n in range(number, 0, -1):
        coefs *= n
    return coefs


def calcBinomial(n: int, k: int) -> int:
    produto = fatorial(n) // (fatorial(k) * fatorial(n - k))
    return int(produto)


binomialNumber = calcBinomial(5, 3)
print(binomialNumber)
