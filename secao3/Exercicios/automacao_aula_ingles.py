import datetime
import sys

# só roda se for terça-feira
if datetime.datetime.today().weekday() != 1:
    sys.exit()  # encerra o script se não for terça

import time

try:
    import pyautogui
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyautogui"])
    import importlib
    pyautogui = importlib.import_module("pyautogui")

# try:
#     import keyboard
# except ImportError:
#     import subprocess
#     subprocess.check_call([sys.executable, "-m", "pip", "install", "keyboard"])
#     import importlib
#     keyboard = importlib.import_module("keyboard")


def tarefa():
    time.sleep(1)
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('chrome')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('https://meet.google.com/tir-degt-esq')
    pyautogui.press('enter')
    time.sleep(3)


tarefa()
# keyboard.add_hotkey('ctrl+alt+shift+e', tarefa)
# keyboard.wait('esc')