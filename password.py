import tkinter as tk
import random
from tkinter import font
from tkinter.ttk import Combobox
from tkinter import Button, Entry, Label, Tk, messagebox
from tkinter.font import Font

win = Tk()
win.title("Password Generator")
win.geometry("600x300+250+50")
win.resizable(False, False)

# Configure Poppins font
font_style = font.Font(family="Poppins", size=10)

def generate_password():
    password = ''
    try:
        length = int(password_length_entry.get())
        difficulty = password_complexity_combobox.current()
        if length <= 5 or length > 25:
            messagebox.showinfo("Invalid Length", "Please provide length in between 6 to 25")
            return
        else:
            if difficulty == -1:
                messagebox.showinfo("Invalid difficulty", "Please provide difficulty of password")
                return
            if difficulty == 0:  # Easy
                password = generate_easy_password(length)
            elif difficulty == 1:  # Medium
                password = generate_medium_password(length)
            elif difficulty == 2:  # Difficult
                password = generate_difficult_password(length)
                
            password_label.config(text=password)
    except ValueError:
        messagebox.showinfo("Invalid Length", "Please provide valid value")

def generate_easy_password(length):
    return ''.join(random.choices('0123456789', k=length))

def generate_medium_password(length):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    return ''.join(random.choices('0123456789' + alpha, k=length))

def generate_difficult_password(length):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    symbols = "!@#$%^&*()-+;:'\|,<.>/?`~"
    return ''.join(random.choices('0123456789' + alpha + symbols, k=length))

password_length_label = Label(win, text="Enter length of password(6-25)", font=("candara", 15, 'bold'))
password_length_label.place(x=10, y=30)
password_length_entry = Entry(win, font=('lucida', 15))
password_length_entry.place(x=320, y=30)

password_complexity_label = Label(win, text="Set Password Complexity", font=("candara", 15, 'bold'))
password_complexity_label.place(x=10, y=90)
password_complexity_combobox = Combobox(win,values=['Easy (Only Int)','Medium (Int + Alphabets)','Hard (Int + Alphabets + Symbols)'])
password_complexity_combobox.config(width=30, justify='center')
password_complexity_combobox.place(x=320, y=95)

generate_button = Button(win, text="Generate", font=("candara", 15, 'bold'), command=generate_password)
generate_button.place(x=250, y=150)

password_label_text = Label(win, text="Password", font=("candara", 15, 'bold'))
password_label_text.place(x=200, y=220)

password_label = Label(win, text="- - - - -", font=("candara", 15, 'bold'))
password_label.place(x=320, y=220)

credit_label = tk.Label(win, text='Code By Gayathri Vaddi', wraplength=400,
                        font=Font(family='Poppins', size=12, weight='bold'), fg="red")
credit_label.pack()

win.mainloop()