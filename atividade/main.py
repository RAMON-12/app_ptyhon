import os  # Corrected import statement

# Lista de notas
notas = []

# Algoritmo
try:
    while True:
        try:
            nota = float(input("Informe a nota do aluno: ").replace(",", "."))
            if 0 <= nota <= 10:
                notas.append(nota)
                print("Nota inserida com sucesso.")
            else:
                print("Nota inválida. Favor insira uma nota")
                continue
        except ValueError:
            print("Entrada inválida. Favor insira um número válido.")
            continue

        while True:
            continuar = input("Deseja continuar inserindo notas? (s/n): ")
            if continuar in ["s", "n"]:
                os.system("cls")  
            else:
                print("Opção inválida. Digite 's' para sim ou 'n' para não.")

        if continuar == "n":
            break

    for i, nota in enumerate(notas):
        print(f"Nota {i + 1}: {nota}.")

    media = sum(notas) / len(notas)

except ValueError as e:
    print(f"Não foi possível inserir as notas e calcular a média. {e}.")
else:
    print(f"A média das notas é: {media:.2f}.")
    if media >= 7:
        print("O aluno está aprovado.")
    elif media >= 5:
        print("O aluno está de recuperação.")
    else:
        print("O aluno está reprovado.")
finally:
    print("Encerrando o programa.")
        

