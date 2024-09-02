import concurrent.futures
import os.path
import window_control
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


bots = {}  # title: window_control

executor = concurrent.futures.ThreadPoolExecutor()


def create_new_bot(title):
    global bots, horizontal_blocks, vertical_blocks, bots_table
    bot = window_control.Window(title, mine_key, horizontal_blocks=int(horizontal_blocks.get()), vertical_blocks=int(vertical_blocks.get()))
    bots[title] = bot
    bot.thread = executor.submit(bot.mine)

    mc_title = tk.Label(bots_table, text=title)
    mc_title.grid(row=bots_table.grid_size()[1], column=0, padx=5, pady=5)

    mc_stop_button = tk.Button(bots_table, text='Stop', command=lambda: stop_bot(title, mc_title, mc_stop_button))
    mc_stop_button.grid(row=bots_table.grid_size()[1]-1, column=1, padx=5, pady=5)


def stop_bot(title, mc_title, mc_stop_button):
    bots.pop(title).active = False
    mc_title.destroy()
    mc_stop_button.destroy()



root = tk.Tk()
root.title("KopaczMC")
root.geometry("800x600")
root.resizable(False, False)

bg_file = Image.open(os.path.join('assets', 'bg.png'))
background_image = ImageTk.PhotoImage(bg_file)

canvas = tk.Canvas(root, width=bg_file.width, height=bg_file.height)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_image, anchor="nw")

windows = window_control.list_of_windows()
selected_window = tk.StringVar()
dropdown_windows = ttk.Combobox(root, textvariable=selected_window, values=windows, width=30)
dropdown_windows.place(x=190, y=38)

horizontal_blocks = tk.StringVar()
horizontal_blocks_input = tk.Entry(root, textvariable=horizontal_blocks, width=5)
horizontal_blocks_input.place(x=190, y=72)

vertical_blocks = tk.StringVar()
vertical_blocks_input = tk.Entry(root, textvariable=vertical_blocks, width=5)
vertical_blocks_input.place(x=250, y=72)

mine_key = tk.StringVar()
mine_key_input = tk.Entry(root, textvariable=mine_key, width=5)
mine_key_input.place(x=190, y=106)

button_create_new_bot = ttk.Button(root, text="Dodaj Bota", command=lambda: create_new_bot(selected_window.get()))
button_create_new_bot.place(x=150, y=250)

bots_table = tk.Frame(root)
bots_table.place(x=450, y=40)


root.mainloop()

executor.shutdown(wait=False)

for window in bots.values():
    window.active = False
