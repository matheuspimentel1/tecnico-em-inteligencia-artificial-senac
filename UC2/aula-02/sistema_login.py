usuario = input("Usuário: ")
senha = input("Senha: ")

if usuario != "Admin":
    print()
    print("Usuário incorreto.")

elif senha != "1234":
    print()
    print("Senha incorreta.")

else:
    print()
    print("Login realizado com sucesso.")