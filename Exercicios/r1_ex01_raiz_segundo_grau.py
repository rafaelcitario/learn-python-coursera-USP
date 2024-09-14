import math

# from time import sleep
# import random

descriminante = {
    "a": int(input("digite o valor de a: ")),
    "b": int(input("digite o valor de b: ")),
    "c": int(input("digite o valor de c: ")),
}


# def loadingCalculation():
#     messages = [
#         "Carregando...",
#         "Descriminando delta...",
#         "Realizando raízes...",
#         "Concluído",
#     ]
#     for state in range(len(messages)):
#         print(messages[state])
#         sleep(random.random() * random.randint(0, 3))
#         if state == 3:
#             return "OK"


def resolveQuadraticEquation(descriminante):
    # loadingStats = loadingCalculation()
    # if loadingStats != "OK":
    #     return exec("clear")

    delta = (
        math.pow(descriminante["b"], 2) - 4 * descriminante["a"] * descriminante["c"]
    )
    if delta < 0:
        return "esta equação não possui raízes reais"

    x1 = (-descriminante["b"] + math.sqrt(delta)) / (2 * descriminante["a"])
    x2 = (-descriminante["b"] - math.sqrt(delta)) / (2 * descriminante["a"])

    if delta == 0:
        result = "a raiz dupla desta equação é %d" % x1
        return result

    if x1 > x2:
        result = "as raízes da equação são %d e %d" % (x1, x2)
        return result

    result = "as raízes da equação são %d e %d" % (x2, x1)
    # result = {"delta": delta, "x1": x1, "x2": x2}
    return result


quadraticEquation = resolveQuadraticEquation(descriminante)
# message = (
#     "\n\n\tDelta: %d\n\tX1: %d\n\tX2: %d"
#     % (
#         quadraticEquation["delta"],
#         quadraticEquation["x1"],
#         quadraticEquation["x2"],
#     )
#     if type(quadraticEquation) != type("str")
#     else "\n\n\t%s" % (quadraticEquation)
# )
print(quadraticEquation)
