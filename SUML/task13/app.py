import random

import tkinter as tk
import numpy as np

window = tk.Tk()
window.title("SUML TASK 13")
window.minsize(300, 300)

def gen_random():
    return random.randint(0, 5)


def handle_button_press(event):
    arr = np.array([[gen_random(), gen_random(), gen_random(), gen_random()],
                    [gen_random(), gen_random(), gen_random(), gen_random()]])
    print(arr)
    label = tk.Label(window, text="Calculations have been performed")
    label.pack()


button = tk.Button(text="Calculate")
button.bind("<Button-1>", handle_button_press)
button.pack()

# Start the event loop.
window.mainloop()
