import ctypes
from ctypes import wintypes

# Definicje struktur i stałych
INPUT_MOUSE = 0
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004


class MOUSEINPUT(ctypes.Structure):
    _fields_ = [("dx", wintypes.LONG),
                ("dy", wintypes.LONG),
                ("mouseData", wintypes.DWORD),
                ("dwFlags", wintypes.DWORD),
                ("time", wintypes.DWORD)]


class INPUT(ctypes.Structure):
    _fields_ = [("type", wintypes.DWORD),
                ("mi", MOUSEINPUT)]


def send_mouse_input(x, y):
    # Ustawienie struktury INPUT
    input_struct = INPUT()
    input_struct.type = INPUT_MOUSE
    input_struct.mi.dx = x
    input_struct.mi.dy = y
    input_struct.mi.mouseData = 0
    input_struct.mi.dwFlags = MOUSEEVENTF_LEFTDOWN
    input_struct.mi.time = 0
    input_struct.mi.dwExtraInfo = 0

    # Wysyłanie wciśnięcia lewego przycisku myszy
    ctypes.windll.user32.SendInput(1, ctypes.byref(input_struct), ctypes.sizeof(input_struct))

    # Ustawienie struktury INPUT na zwolnienie lewego przycisku myszy
    input_struct.mi.dwFlags = MOUSEEVENTF_LEFTUP
    ctypes.windll.user32.SendInput(1, ctypes.byref(input_struct), ctypes.sizeof(input_struct))


if __name__ == "__main__":
    # Przykładowe współrzędne (x, y)
    x = 0
    y = 0
    send_mouse_input(x, y)
