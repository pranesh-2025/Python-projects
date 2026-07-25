import tkinter as tk
from tkinter import messagebox
import math

# -----------------------------
# Function to save history
# -----------------------------
def save_history(expression, result):
    with open("history.txt", "a") as file:
        file.write(f"{expression} = {result}\n")

# -----------------------------
# Button Click
# -----------------------------
def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# -----------------------------
# Clear Screen
# -----------------------------
def clear():
    entry.delete(0, tk.END)

# -----------------------------
# Calculate
# -----------------------------
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        save_history(expression, result)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        messagebox.showerror("Error", "Invalid Expression")

# -----------------------------
# Square Root
# -----------------------------
def sqrt():
    try:
        value = float(entry.get())
        result = math.sqrt(value)
        save_history(f"√({value})", result)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        messagebox.showerror("Error", "Invalid Input")

# -----------------------------
# Percentage
# -----------------------------
def percentage():
    try:
        value = float(entry.get())
        result = value / 100
        save_history(f"{value}%", result)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        messagebox.showerror("Error", "Invalid Input")

# -----------------------------
# Sin
# -----------------------------
def sin():
    try:
        value = math.radians(float(entry.get()))
        result = math.sin(value)
        save_history(f"sin({entry.get()})", result)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        messagebox.showerror("Error", "Invalid Input")

# -----------------------------
# Cos
# -----------------------------
def cos():
    try:
        value = math.radians(float(entry.get()))
        result = math.cos(value)
        save_history(f"cos({entry.get()})", result)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        messagebox.showerror("Error", "Invalid Input")

# -----------------------------
# Tan
# -----------------------------
def tan():
    try:
        value = math.radians(float(entry.get()))
        result = math.tan(value)
        save_history(f"tan({entry.get()})", result)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        messagebox.showerror("Error", "Invalid Input")

# -----------------------------
# Log
# -----------------------------
def log():
    try:
        value = float(entry.get())
        result = math.log10(value)
        save_history(f"log({value})", result)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        messagebox.showerror("Error", "Invalid Input")

# -----------------------------
# GUI Window
# -----------------------------
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("420x520")

entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
    ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
    ('0',4,0),('.',4,1),('+',4,2),('=',4,3),
]

for (text,row,col) in buttons:
    if text == "=":
        tk.Button(root,text=text,width=8,height=2,font=("Arial",12),
                  command=calculate).grid(row=row,column=col)
    else:
        tk.Button(root,text=text,width=8,height=2,font=("Arial",12),
                  command=lambda t=text: click(t)).grid(row=row,column=col)

tk.Button(root,text="Clear",width=8,height=2,command=clear).grid(row=5,column=0)
tk.Button(root,text="√",width=8,height=2,command=sqrt).grid(row=5,column=1)
tk.Button(root,text="%",width=8,height=2,command=percentage).grid(row=5,column=2)
tk.Button(root,text="^",width=8,height=2,
          command=lambda: click("**")).grid(row=5,column=3)

tk.Button(root,text="sin",width=8,height=2,command=sin).grid(row=6,column=0)
tk.Button(root,text="cos",width=8,height=2,command=cos).grid(row=6,column=1)
tk.Button(root,text="tan",width=8,height=2,command=tan).grid(row=6,column=2)
tk.Button(root,text="log",width=8,height=2,command=log).grid(row=6,column=3)

root.mainloop()
import math

degree_mode = True

def sin_value(x):
    if degree_mode:
        x = math.radians(x)
    return math.sin(x)