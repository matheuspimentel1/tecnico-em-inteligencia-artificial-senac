import random

ia = random.randint(0, 2)

print(f"""
    JOGO DO PEDRA PAPEL TESOURA
    ---------------------------
    0 - Pedra
    1 - Papel
    2 - Tesoura
""")

opcao = int(input("Digite a alternativa desejada: "))

if (opcao == 0 and ia == 2) or (opcao == 1 and ia == 0) or (opcao == 2 and ia == 1):
    print("Parabéns você ganhou!")

elif (opcao == 0 and ia == 1) or (opcao == 1 and ia == 2) or (opcao == 2 and ia == 0):
    print("snébaraP você perdeu!")

else:
    print("Empatou.")