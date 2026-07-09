import pandas as pd
import pyautogui
import time

pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

planilha = pd.read_excel("trabalhoautomacao/certificados.xlsx")
time.sleep(5) 

for linha in range(len(planilha)):
    nome = str(planilha.loc[linha, "Nome"])
    curso = str(planilha.loc[linha, "Curso"])
    carga = str(planilha.loc[linha, "Carga Horária"])
    data = str(planilha.loc[linha, "Data"])

    campo_nome = pyautogui.locateCenterOnScreen("campo_nome.png", confidence=0.8)
    if not campo_nome:
        print(f"Campo Nome não encontrado na linha {linha}")
        continue

    pyautogui.click(campo_nome)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    pyautogui.write(nome)

    campo_data = pyautogui.locateCenterOnScreen("campo_data.png", confidence=0.8)

    if not campo_data:
        print(f"Campo Data não encontrado na linha {linha}")
        continue

    pyautogui.click(campo_data)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    pyautogui.write(data)

    campo_carga = pyautogui.locateCenterOnScreen("campo_carga.png", confidence=0.8)
    
    if not campo_carga:
        print(f"Campo Carga Horária não encontrado na linha {linha}")
        continue

    pyautogui.click(campo_carga)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    pyautogui.write(carga)

    campo_curso = pyautogui.locateCenterOnScreen("campo_curso.png", confidence=0.8)
    
    if not campo_curso:
        print(f"Campo Curso não encontrado na linha {linha}")
        continue

    pyautogui.click(campo_curso)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    pyautogui.write(curso)
    
    botao_enviar = pyautogui.locateCenterOnScreen("botao_enviar.png", confidence=0.8)
    
    if not botao_enviar:
        print(f"Botão Enviar não encontrado na linha {linha}")
        continue
    
    pyautogui.click(botao_enviar)
    print(f"Linha {linha} enviada com sucesso")
    
    time.sleep(2)