# entrada de dados:
# nome, dia vencimento, mês vencimento, valor fatura


import locale

locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")


UserInfo = {
    "name": input("Digite o nome do cliente: "),
    "dateLimit": input("Digite o dia de vencimento: "),
    "monthLimit": input("Digite o mês de vencimento: "),
    "debit": input("Digite o valor da fatura: "),
}


def formatDebit(debit):
    for digit in debit:
        if digit == "." or digit == ",":
            debit = str.replace(debit, ".", "")
            debit = str.replace(debit, ",", "")

    debit = debit[:-2] + "." + debit[-2:]
    return debit


def invoice(UserInfo):
    formatedDebit = formatDebit(UserInfo["debit"])
    # saida de dados:
    # Olá, Fulano de Tal
    # A sua fatura com vencimento em 9 de Janeiro no valor de R$ 350,00 está fechada.
    message = (
        "Olá, %s\nA sua fatura com vencimento em %s de %s no valor de R$ %s está fechada."
        % (
            UserInfo["name"],
            UserInfo["dateLimit"],
            UserInfo["monthLimit"],
            locale.currency(
                float(formatedDebit),
                symbol=False,
                grouping=True,
                international=True,
            ),
        )
    )
    return message


formatedInvoice = invoice(UserInfo)
print(formatedInvoice)
