import math

squareSide = int(input("Digite o valor correspondente ao lado de um quadrado: "))


def squareArea(sidesSquare):
    area = math.pow(sidesSquare, 2)
    return area


def squarePerimeter(sidesSquare):
    perimeter = sidesSquare * 4
    return perimeter


perimeter = squarePerimeter(squareSide)
area = squareArea(squareSide)
# perímetro: 12 - área: 9
print("perímetro: %d - área: %d" % (perimeter, area))
