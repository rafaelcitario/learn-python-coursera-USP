def vogal(letra: str) -> bool:
    vogais = ["a", "e", "i", "o", "u"]
    if vogais.__contains__(str.lower(letra)):
        return True
    return False
