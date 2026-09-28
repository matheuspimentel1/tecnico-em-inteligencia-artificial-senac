peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print()
    print(f"IMC: {imc}")
    print("Classificação: Abaixo do peso.")

elif imc < 25:
    print()
    print(f"IMC: {imc}")
    print("Classificação: Peso normal.")

elif imc < 30:
    print()
    print(f"IMC: {imc}")
    print("Classificação: Sobrepeso.")

else:
    print()
    print(f"IMC: {imc}")
    print("Classificação: Obesidade.")
