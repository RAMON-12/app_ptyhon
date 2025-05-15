# importa bliblioteca
import time 
import modulo as m

# algoritimo principal
if __name__ == "__main__":
    nome = input("informe o nome do aluno: ")
    resultado = m.verificar_matricula(nome)
    for verificacao in resultado:
         time.sleep(3)
