import os.path
import time
from ahk import AHK


def list_of_windows():
    windows = AHK(executable_path=os.path.join('assets', 'AutoHotkey.exe')).windows()
    windows_titles = [window.title for window in windows if len(window.title) > 0]
    return windows_titles


class Window:
    def __init__(self, window_title, mine_key, horizontal_blocks=5, vertical_blocks=1):
        self.mine_key = mine_key
        self.horizontal_blocks = (horizontal_blocks - 1) / 3
        self.vertical_blocks = (vertical_blocks - 1) / 3
        self.active = True
        self.ahk = AHK(executable_path=os.path.join('assets', 'AutoHotkey.exe'))
        self.win = self.ahk.find_window(title=window_title)
        self.visible = True
        self.thread = None

    def change_visible(self):
        if self.visible:
            self.win.hide()
            self.visible = False
        else:
            self.win.show()
            self.visible = True

    def mine(self):
        print('{' + self.mine_key + ' down}')
        self.win.send('{' + self.mine_key + ' down}')
        while self.active:
            self.win.send('{d down}')
            time.sleep(self.horizontal_blocks)
            self.win.send('{d up}')
            self.win.send('{s down}')
            time.sleep(self.vertical_blocks)
            self.win.send('{s up}')
            self.win.send('{a down}')
            time.sleep(self.horizontal_blocks)
            self.win.send('{a up}')
            self.win.send('{w down}')
            time.sleep(self.vertical_blocks)
            self.win.send('{w up}')
        self.win.send('{' + self.mine_key + ' up}')
