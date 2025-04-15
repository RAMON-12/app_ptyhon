nome = input("informe seu nome: ")
nota = float(input("informe sua nota: "))


# veridica se  o aluno passou ou nao
if nota >= 0 and nota < 10:
    if nota >= 7:
        print(f"{nome} esta Aprovado.")
    elif nota >= 5:
        print(f"{nome} esta de Recuperacao.")
    else:
        print(f"{nome} esta Reprovado.")
else:
    print("Nota invalida.")