nota_final = float(input("Digite sua nota: "))
frequencia = int(input("Digite sua frequência: "))

if frequencia < 75:
    print()
    print("Reprovado por frequência")

elif nota_final < 5:
    print()
    print("Reprovado.")

elif nota_final >= 5 and nota_final < 7:
    print()
    print("Recuperação.")

else:
    print()
    print("Aprovado.")