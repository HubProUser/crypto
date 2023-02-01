import pyautogui
from pynput.mouse import Listener

a = 0


def on_click(x, y, button, pressed):
    global a
    while pressed:
        a += 1
        pyautogui.click()
        print(a)
        if a == 100:
            a = 0
            return False


while True:
    with Listener(on_click=on_click) as listener:
        listener.join()