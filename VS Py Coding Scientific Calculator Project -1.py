import tkinter as tk
import math

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry('260*380')  
root.resizable(0,0)
root.configure(background='black')

entry = tk.Entry(root, font="Arial 25", borderwidth=5, relief="ridge", justify="right", state="readonly")
entry.grid(row=0, column=0, columnspan=6, pady=(50,25), sticky="w")
entry.pack(ipadx=1, pady=2, padx=2)

buttons = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["0", ".", "=", "/"],
    ["C", "(", ")", "**"]]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        if btn == "=":
            b = tk.Button(frame, text=btn, font="Arial 16", bg='grey', fg='white', width=4, height=1, command= Calculate)
        elif btn == "C":
            b = tk.Button(frame, text=btn, font="Arial 16", bg='blue', fg='white', width=4, height=1, command= clear)
        else:
            b = tk.Button(frame, text=btn, font="Arial 16", bg='grey', fg='white', width=4, height=1, command=lambda x=btn: add_text(x))
        b.pack(side="left", expand=True, fill="both", padx=1, pady=1)

def set_entry(value):
    entry.config(state="normal")
    entry.delete(0, tk.END)
    entry.insert(tk.END, value)
    entry.config(state="readonly")

def add_text(text):
    entry.config(state="normal")
    entry.insert(tk.END, text)
    entry.config(state="readonly")

def clear(event=None):
    set_entry("")
    
def Calculate(event=None):
    try:
        expression = entry.get()
        result = eval(expression)
        set_entry(str(result))
    except:
        set_entry("Error")
    
root.bind("<Return>", Calculate)
root.bind("<Escape>", clear)
root.bind("<BackSpace>", lambda e: set_entry(entry.get()[:-1]))

for key in "0123456789+-*/().":
    root.bind(key, lambda e, k=key: add_text(k))
 
sci_buttons = [
    ["sqrt", "log", "ln", "fact"],
    ["sin", "cos", "tan", "pi", "e"]
]
for row in sci_buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        if btn == "pi":
            b = tk.Button(frame, text="π", font="Arial 16", bg='grey', fg='white', width=4, height=1, command=lambda: add_text(str(math.pi)))
        elif btn == "e":
            b = tk.Button(frame, text="e", font="Arial 16", bg='grey', fg='white', width=4, height=1, command=lambda: add_text(str(math.e)))
        else:
            b = tk.Button(frame, text=btn, font="Arial 16", bg='grey', fg='white', width=4, height=1, command=lambda x=btn: scientific(x))
        b.pack(side="left", expand=True, fill="both", padx=1, pady=1)
        
def scientific(func):
    try:
        value = float(entry.get())
        if func == "sqrt":
            set_entry(math.sqrt(value))
        elif func == "log":
            set_entry(math.log10(value))
        elif func == "ln":
            set_entry(math.log(value))
        elif func == "sin":
            set_entry(math.sin(math.radians(value)))
        elif func == "cos":
            set_entry(math.cos(math.radians(value)))
        elif func == "tan":
            set_entry(math.tan(math.radians(value)))
        elif func == "fact":
            set_entry(math.factorial(int(value)))
    except:
        set_entry("Error")
        
    root.bind("s", lambda e: scientific("sin"))       # s = sin
    root.bind("c", lambda e: scientific("cos"))       # c = cos
    root.bind("t", lambda e: scientific("tan"))       # t = tan
    root.bind("l", lambda e: scientific("log"))       # l = log10
    root.bind("n", lambda e: scientific("ln"))        # n = log
    root.bind("q", lambda e: scientific("sqrt"))      # q = sqrt
    root.bind("f", lambda e: scientific("fact"))      # f = fact
    root.bind("p", lambda e: add_text(str(math.pi)))  # p = π
    root.bind("e", lambda e: add_text(str(math.e)))   # e = e
        
root.mainloop()