valor_original = float(input("Qual é o valor da compra? "))
desconto = 0
porcentagem = 0

if valor_original <= 100:
    desconto = desconto

elif valor_original <= 300:
    desconto = 0.05
    porcentagem = 5

elif valor_original <= 500:
    desconto = 0.1
    porcentagem = 10

else:
    desconto = 0.15
    porcentagem = 15

valor_desconto = valor_original * desconto
valor_final = valor_original - valor_desconto

print()
print(f"Valor original: {valor_original}")
print(f"Desconto: {porcentagem} %")
print(f"Valor do desconto: {valor_desconto}")
print(f"Valor final: {valor_final}")
print()