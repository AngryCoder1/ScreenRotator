import rotatescreen
import ctypes
import webbrowser
from time import sleep


def madness():
    ctypes.windll.user32.MessageBoxW(0, "Press 'OK' to get your prize!", "Congratulations!", 0)
    webbrowser.open_new_tab("<YOUR_SOCIAL_NETWORK>")
    for i in range(0, 1030):
        rotatescreen.get_primary_display().rotate_to(abs((rotatescreen.get_primary_display().current_orientation - i * 90) % 360))
        sleep(0.1)
    ctypes.windll.user32.MessageBoxW(0, "It looks crazy, right?\nMade by <YOUR_NAME>", "Congratulations! You've been trolled!", 0)


madness()
# build: pyinstaller.exe --onefile --windowed --icon=icon.ico main.py
