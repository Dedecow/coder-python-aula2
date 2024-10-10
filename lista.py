frutas = [maça, banana, uva, pera]

def mostra_fruta():
    print("\nLista de frutas: " )
    for fruta in frutas:
        print(f" -{fruta}")
    print()

def add_fruta():
    fruta= input("Adicione uma fruta: ")

    if fruta in frutas:
        print("Fruta já existe. Digitação desconsiderada.")
    else:
        frutas.append(fruta)
        print("Fruta adicionada com sucesso.")

add_fruta()
mostra_fruta()