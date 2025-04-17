novovalor = "s"
while novovalor == "s":
    n = int(input("Digite um valor: "))

    if n % 2 == 0:
        print(f"{n} é par")
    else:
        print(f"{n} é ímpar")
    if n < 0:
        print(f"{n} é negativo e par")
    else:
        print(f"{n} é positvo")

    novovalor=input("Deseja fazer o cálculo novamente? (s/n)")
