def maximo(*args: int) -> int:
    max_value = args[0]

    for argument in args:
        if argument > max_value:
            max_value = argument

    return max_value
