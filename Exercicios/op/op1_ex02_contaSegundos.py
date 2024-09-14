def convertSeconds():
    dataSeconds = int(
        input("Por favor, entre com o número de segundos que deseja converter: ")
    )

    tempElements = {"seconds": 0, "minutes": 0, "hours": 0, "days": 0}
    for key in tempElements:

        if key == "days":
            tempElements[key] = dataSeconds // 24
            continue

        if key != "hours":
            tempElements[key] = dataSeconds % 60
            dataSeconds //= 60
            continue

        tempElements[key] = dataSeconds % 24

    formatedMessage = "%d dias, %d horas, %d minutos e %d segundos." % (
        tempElements["days"],
        tempElements["hours"],
        tempElements["minutes"],
        tempElements["seconds"],
    )
    return formatedMessage


convertedData = convertSeconds()
print(convertedData)
