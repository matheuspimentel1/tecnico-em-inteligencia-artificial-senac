nivel = int(input("Digite o seu nível: "))
espada = bool(input("Possui espada? "))
cajado = bool(input("Possui cajado? "))

if nivel >= 10 and (espada or cajado) == True:
    print()
    print("O personagem pode entrar na Dungeon!")

else:
    print()
    print("O personagem NÃO pode entrar!")