import tkinter as tk
from tkinter import ttk, messagebox
import string
import random

# Define the character sets
UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
DIGITS = string.digits
SYMBOLS = string.punctuation
AMBIGUOUS = 'il1Lo0O'

# Function to calculate password strength
def calculate_strength(password):
    length = len(password)
    variety = len(set(password))
    if length >= 12 and variety > 8:
        return "Strong", "green"
    elif length >= 8:
        return "Medium", "orange"
    else:
        return "Weak", "red"

# Password generation logic
def generate_password():
    length = length_var.get()
    include_upper = upper_var.get()
    include_lower = lower_var.get()
    include_digits = digits_var.get()
    include_symbols = symbols_var.get()
    exclude_ambiguous = ambiguous_var.get()

    character_pool = ''
    if include_upper:
        character_pool += UPPERCASE
    if include_lower:
        character_pool += LOWERCASE
    if include_digits:
        character_pool += DIGITS
    if include_symbols:
        character_pool += SYMBOLS

    if exclude_ambiguous:
        character_pool = ''.join([c for c in character_pool if c not in AMBIGUOUS])

    if not character_pool:
        messagebox.showwarning("Selection Error", "Please select at least one character type.")
        return

    password = ''.join(random.choice(character_pool) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    strength, color = calculate_strength(password)
    strength_label.config(text=f"Strength: {strength}", foreground=color)

# Copy to clipboard
def copy_to_clipboard():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard.")

# GUI setup
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x400")
root.resizable(False, False)

# Password display
password_entry = tk.Entry(root, font=("Arial", 14), width=30, bd=2)
password_entry.pack(pady=10)

# Length slider
length_var = tk.IntVar(value=12)
tk.Label(root, text="Password Length").pack()
tk.Scale(root, from_=6, to=32, orient="horizontal", variable=length_var).pack()

# Character options
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)
ambiguous_var = tk.BooleanVar(value=False)

options = [
    (upper_var, "Include Uppercase Letters"),
    (lower_var, "Include Lowercase Letters"),
    (digits_var, "Include Digits"),
    (symbols_var, "Include Symbols"),
    (ambiguous_var, "Exclude Ambiguous Characters"),
]

for var, text in options:
    ttk.Checkbutton(root, text=text, variable=var).pack(anchor='w', padx=20)

# Buttons
ttk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)
ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)

# Strength label
strength_label = tk.Label(root, text="Strength: ", font=("Arial", 12))
strength_label.pack(pady=10)

root.mainloop()
