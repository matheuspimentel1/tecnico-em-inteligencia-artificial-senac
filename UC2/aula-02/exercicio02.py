lado1 = int(input("Qual é o tamanho do lado 1? "))
lado2 = int(input("Qual é o tamanho do lado 2? "))
lado3 = int(input("Qual é o tamanho do lado 3? "))

if lado1 == lado2 and lado1 == lado3:
    print("Triângulo Equilátero")

elif lado1 == lado2 or lado1 == lado3:
    print("Triângulo Isósceles")

else:
    print("Triângulo Escaleno")