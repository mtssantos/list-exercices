numero_macas = int(input("Informe o número de maças: "))

total = 0.0

if (numero_macas < 12):
    total = numero_macas * 1.30
elif (numero_macas >= 12):
    total = numero_macas * 1.00

print(f"Valor total: R$ {total}")