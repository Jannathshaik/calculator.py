import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

window = tk.Tk()
window.title('Simple Calculator')

frame = tk.Frame(master=window, bg="lightblue", padx=20)
frame.pack()

entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=8, width=50)
entry.grid(row=0, column=0, columnspan=4, ipady=2, pady=2)


def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))


def button_clear():
    entry.delete(0, tk.END)


def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        tkinter.messagebox.showinfo("Error", "Invalid Input")


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_num, col_num = 1, 0

for button_text in buttons:
    if button_text == 'C':
        button = tk.Button(master=frame, text=button_text, padx=15, pady=5, width=3, command=button_clear)
    elif button_text == '=':
        button = tk.Button(master=frame, text=button_text, padx=15, pady=5, width=3, command=button_equal)
    else:
        button = tk.Button(master=frame, text=button_text, padx=15, pady=5, width=3, command=lambda num=button_text: button_click(num))
    button.grid(row=row_num, column=col_num, pady=2)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

window.mainloop()
