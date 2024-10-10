def asterisco_por_vogal(frase):
    vogais = "aAeEiIoOuU"
    nova_frase = ""

    for letra in frase:
        if letra in vogais:
            nova_frase += "*"
        else:
            nova_frase += letra
    return nova_frase