import math

pontos = {}

for i in range(0, 4):
    isNotEven = i % 2 != 0
    keys = "y" if isNotEven else "x"
    pontos[keys + "%d" % i] = float(
        input(
            "Digite um valor número que represente a posição do ponto no eixo %s%d: "
            % (keys, i)
        )
    )

for k in pontos.keys():
    swap = {}
    if not str.startswith(k, "x"):
        swap[0] = pontos[k]
        pontos.pop(k)
        pontos[k] = swap[0]

stack = []
for e in pontos.keys():
    if str.startswith(e, "x"):
        stack.append(pontos[e])
        continue
    stack.append(pontos[e])

equation = math.sqrt(
    math.pow(stack[1] - stack[0], 2) + math.pow(stack[3] - stack[2], 2)
)

distancia = "perto" if equation < 10 else "longe"
print("%s" % distancia)
