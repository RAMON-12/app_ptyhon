#crie um program que comita o prokero de voces e envie o repositório para o github
import pyautogui as p



def limpa_credciais():
    p.write("git config --global --unset user.name")
    p.press("enter")
    p.write("git config --global --unset user.email")
    p.press("enter")

if __name__ == "__main__":
    p.PAUSE = 0.5
msg_commit = input("Digite a mensagem do commit: ")

limpa_credciais()

p.typewrite("git status")
p.press("enter")
p.typewrite("git add .")
p.press("enter")
p.typewrite(f"git commit -m '{msg_commit}'")
p.press("enter")
p.typewrite("git push")
p.press("enter")

