import pyautogui
import time
import pandas
import pandas as pd

#pyautogui.click -> clica em algum lugar
#pyautogui.press -> aperta 1 tecla
#pyautogui.write -> escrever um  texto

pyautogui.PAUSE = 1.2 # delay

# 1 - entrando no sistema
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#espera 3 segundos
time.sleep(3)

# 2 - fazendo login
pyautogui.click(x=456, y=373)
pyautogui.write("loginexemplo@gmail.com")
#senha
pyautogui.press("tab")
pyautogui.write("123457")
#logar
pyautogui.press("tab")
pyautogui.press("enter")

#espera 3 segundos
time.sleep(3)

# 3 - importando base de dados
tabela = pandas.read_csv("produtos.csv")

# 4 - cadastrando os produtos

for linha in tabela.index:
    pyautogui.click(x=463, y=255)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs_valor = tabela.loc[linha, "obs"]
    
    if pd.isna(obs_valor):
        obs = ""
    else:
        obs = str(obs_valor)  

    pyautogui.write(obs)
    pyautogui.press("enter") # enviar   
    pyautogui.scroll(10000)


