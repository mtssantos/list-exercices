nome = input("Diga seu nome: ")
genero = input("Informe o seu gênero: ")


if (genero.upper() == "FEMININO"):
    print(f"Ilmo Sra. {nome}")
elif (genero.upper() == "MASCULINO"):
    print(f"Ilmo Sr. {nome}")
else:
    print("Não definido!")