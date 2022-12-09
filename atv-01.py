nome_aluno = input("Digite seu nome: ")
nota_um = float(input("Digite a nota do primeiro bimestre: "))
nota_dois = float(input("Digite a nota do segundo bimestre: "))
nota_tres = float(input("Digite a nota do terceiro bimestre: "))
nota_quatro = float(input("Digite a nota do quarto bimestre: "))
media_aritimetica = (nota_um + nota_dois + nota_tres + nota_quatro) / 4

print(f"""
  Olá, {nome_aluno}.
  Sua nota no primeiro bimestre foi: {nota_um}
  Sua nota no segundo bimestre foi: {nota_dois}
  Sua nota no terceiro bimestre foi: {nota_tres}
  Sua nota no quarto bimestre foi: {nota_quatro}

  -------------------------------------------------
  Portanto, sua média aritimética é: {round(media_aritimetica, 2)}

""")
