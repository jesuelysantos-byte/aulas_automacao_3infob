import pyautogui
import pandas as pd
import time

def preencher(image, deslocamentoY = 0, valor = None):
    campo = pyautogui.locateCenterOnScreen(image, confidence=0.9)
    pyautogui.click(campo.x, campo.y + deslocamentoY)
    if valor:
        pyautogui.write(valor)
    pyautogui.scroll(-150)
    time.sleep(1)

#variaveis
Nome = "Jesuely"
Matricula = "2024190042"
Curso = "Info"
Genero = "F"


preencher("aula12\\Registrar.png")
preencher("aula12\\Nome.png", 55, Nome)
preencher("aula12\\Numero.png", 55, Matricula)
preencher("aula12\\Curso.png", 55, Curso)
preencher(f"aula12\\(Genero).png")
preencher("aula12\\Enviar.png")