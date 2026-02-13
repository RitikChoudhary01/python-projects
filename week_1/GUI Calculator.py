import tkinter as tk

# ---------------- Functions ----------------
def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(key))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# ---------------- Window ----------------
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# ---------------- Entry ----------------
entry = tk.Entry(
    root,
    font=("Arial", 20),
    borderwidth=5,
    relief="ridge",
    justify="right"
)
entry.pack(fill="x", padx=10, pady=10)

# ---------------- Buttons ----------------
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

frame = tk.Frame(root)
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")
    for char in row:
        btn = tk.Button(
            row_frame,
            text=char,
            font=("Arial", 16),
            command=lambda c=char: calculate() if c == '=' else press(c),
            height=2,
            width=5
        )
        btn.pack(side="left", expand=True, fill="both")

# Clear button
clear_btn = tk.Button(
    root,
    text="C",
    font=("Arial", 16),
    command=clear,
    height=2
)
clear_btn.pack(fill="x", padx=10, pady=5)

# ---------------- Run ----------------
root.mainloop()
