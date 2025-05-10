#1. Abrir o navegador e entrar na página do jogo (https://gameforge.com/en-US/littlegames/magic-piano-tiles/#)
#2. Iniciar o game
#3. Clicar nos botões pretos para jogar
#4. Definir um botão para pausar a automação


import pyautogui
from time import sleep
import keyboard
import webbrowser
import win32api
import win32con

webbrowser.open('https://gameforge.com/en-US/littlegames/magic-piano-tiles/#')
sleep(7)
pyautogui.click(543,417, duration=1)
sleep(7)
pyautogui.click(538,376, duration=1)


#define o que fazer com o click
def click(x,y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

#criar um botão para desativar a automação, caso o botão 1 seja pressionado (true)
while keyboard.is_pressed('1') == False:
    #pega a coordenada do pixel (usando mouseInfo e a cor rgb)
    if pyautogui.pixelMatchesColor(446,399,(0,0,0)): 
        click(446,399)
    if pyautogui.pixelMatchesColor(508,399,(0,0,0)):
        click(508,399)
    if pyautogui.pixelMatchesColor(577,399,(0,0,0)):
        click(577,399)
    if pyautogui.pixelMatchesColor(635,399,(0,0,0)):
        click(635,399)


