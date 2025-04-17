# importa blibliotecas
import calendar 
from datetime import date

# declaração de variaveis

mes = date.today().month
ano = date.today().year

# imprimr o calendario do mes 

print(calendar.month(ano, mes))