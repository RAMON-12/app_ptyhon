# tupla 
dias_semana = ("domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sábado")

# lista de tupla
for dia in dias_semana:
    print(dia)

try:

# tetativa de fazer operações de tupla

    dias_semana.append("setima")

    print("\n")
    for dia in dias_semana:
        print(dia)
except Exception as e:
    print(f"nao foi possivel inserir item na tupla: {e}.")

