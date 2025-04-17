a = int(input("Digite o valor A:"))
b = int(input("Digite o valor B:"))
c = int(input("Digite o valor C:"))

soma = a + b
if soma < c:
    print(f"{soma} é menor que c")
else:
    print(f"{soma} não é menor que c")