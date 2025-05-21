#crie um program que comita o prokero de voces e envie o repositório para o github
import pyautogui as auto 

auto.PAUSE = 2


auto.press("win")
auto.typewrite("vscode")
auto.press("enter")
auto.hotkey("ctrl", "j")
auto.typewrite("git status")
auto.press("enter")
auto.typewrite("git add .")
auto.press("enter")
auto.typewrite("git commit -m 'atividade automacao'")
auto.press("enter")
auto.typewrite("git push")
auto.press("enter")
