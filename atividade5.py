peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))

imc = peso/altura**2

if imc < 18.6:
    print(f"seu imc {imc} está abaixo do peso")
elif imc == 18.6 or imc <= 24.9:
    print(f"seu imc {imc} está no peso ideal")
elif imc == 25 or imc <= 29.9:
    print(f"seu imc {imc} está levemente acima do peso")
elif imc == 30 or imc <= 34.9:
    print(f"seu imc {imc} é obesidade grau I")
elif imc == 35 or imc <= 39.9:
    print(f"seu imc {imc} é obesidade grau II (severa)")
else:
    print(f"seu imc {imc} é obesidade grau III (mórbida)")


