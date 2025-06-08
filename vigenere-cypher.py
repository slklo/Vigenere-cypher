import tkinter as tk
from tkinter import messagebox, ttk

class VigenereCipher:
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, text):
        result = ''
        key_len = len(self.key)

        for i, x in enumerate(text):
            if x in self.alphabet:
                t_i = self.alphabet.index(x)
                k_i = self.alphabet.index(self.key[i % key_len])
                result += self.alphabet[(t_i + k_i) % len(self.alphabet)]
            else:
                result += x
        return result

    def decode(self, text):
        result = ''
        key_len = len(self.key)
        a_len = len(self.alphabet)

        for i, x in enumerate(text):
            if x in self.alphabet:
                t_i = self.alphabet.index(x)
                k_i = self.alphabet.index(self.key[i % key_len])
                result += self.alphabet[(t_i - k_i + a_len) % a_len]
            else:
                result += x
        return result

alphabets = {
    "english": "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
    "russian": "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя",
    "eng + rus + symbols": (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz"
        "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        "0123456789.,!?()[]{}<>:;+-=*/_@#$%^&"
    )
}

def process_action():
    text = text_entry.get()
    key = key_entry.get()
    alphabet = alphabets[alphabet_var.get()]
    operation = mode_var.get()

    if not text or not key:
        messagebox.showwarning("Missing input", "Please fill in both text and key.")
        return

    cipher = VigenereCipher(key, alphabet)

    if operation == "encode":
        result = cipher.encode(text)
    else:
        result = cipher.decode(text)

    output_entry.delete(0, tk.END)
    output_entry.insert(0, result)



root = tk.Tk()
root.title("Your title name")
root.geometry("450x200") 
root.wm_attributes('-alpha', 0.85)
root.resizable(width=False,height=False)


tk.Label(root, text="text:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
text_entry = tk.Entry(root, width=60)
text_entry.grid(row=0, column=1, padx=5)

tk.Label(root, text="key:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
key_entry = tk.Entry(root, width=60)
key_entry.grid(row=1, column=1, padx=5)

mode_var = tk.StringVar(value="encode")
tk.Label(root, text="mode:").grid(row=2, column=0, sticky="e")
tk.Radiobutton(root, text="encode", variable=mode_var, value="encode").grid(row=2, column=1, sticky="w")
tk.Radiobutton(root, text="decode", variable=mode_var, value="decode").grid(row=2, column=1, padx=100, sticky="w")

tk.Label(root, text="alphabit:").grid(row=3, column=0, sticky="e")
alphabet_var = tk.StringVar(value="eng + rus + symbols")
alphabet_menu = ttk.OptionMenu(root, alphabet_var, "eng + rus + symbols", *alphabets.keys())
alphabet_menu.grid(row=3, column=1, sticky="w")

tk.Button(root, text="process", command=process_action, width=20).grid(row=4, column=1, pady=10)

tk.Label(root, text="result:").grid(row=5, column=0, sticky="e", padx=5)
output_entry = tk.Entry(root, width=60)
output_entry.grid(row=5, column=1, padx=5)

root.mainloop()
