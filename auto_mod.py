import pyautogui
import time
def ms_auto(nome, a, b):
    pyautogui.press("win")
    pyautogui.write("WhatsApp")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.click(x=627, y=349)
    pyautogui.write(nome)  # inserir o nome da pessoa que irá receber a mensagem
    time.sleep(1)
    pyautogui.click(x=644, y=441)
    time.sleep(0.5)
    pyautogui.write("----Automacao de Gerador de jogos MegaSena----")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.write(f"6 dezenas: {a}, 8 dezenas: {b}")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.write(f" Os jogos foram gerados e enviados usando o Python!")
    pyautogui.press("enter")