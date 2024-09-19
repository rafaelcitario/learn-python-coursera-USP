# 1, 2, 3, 4, 5 = 15
numbers = []

for i in range(0, 5):
    numbers.append(int(input("digite um número: ")))


i = 0
total = 0
while i <= len(numbers) - 1:
    total += numbers[i]
    i += 1

print("Soma da sequencia numérica com while: %d" % total)


j = 0
for number in numbers:
    j += number
print("Soma da sequencia numérica com for: %d" % j)

total = 0
sumSequence = ""
for index in range(0, len(numbers)):
    if numbers[index] != numbers[-1]:
        sumSequence += str(numbers[index]) + "+"
        total += numbers[index]
        continue
    sumSequence += str(numbers[index])
    total += numbers[index]
    print("%s = %d" % (sumSequence, total))
