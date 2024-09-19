numero = int(input("Digite o valor de n: "))

init = 0
for n in range(0, numero):
    for imp in range(init, numero * 2):
        if imp % 2 != 0:
            print(imp)
            init = imp + 1
            break
