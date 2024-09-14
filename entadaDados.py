def convertCelsiusToFahrenheit(celsius):
    fahrenheit = (celsius * 9 + 160) / 5
    return fahrenheit


fahrenheit = convertCelsiusToFahrenheit(1)
print(fahrenheit)


def alternativeFormulaToConvert(temperature):
    celcius = temperature
    if type(celcius) != float and type(celcius) != int:
        return "digite um valor numérico válido"
    fahrenheit = celcius * 1.8 + 32
    return fahrenheit


try:
    celcius = float(input("informe a temperatura em graus celsius: "))
except:
    print("digite um valor numérico válido")

fahrenheit = alternativeFormulaToConvert(celcius)
print(fahrenheit)
