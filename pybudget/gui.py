# pybudget/gui.py

import tkinter as tk
from tkinter import messagebox
from .logic import add_transaction, get_statistics


def on_add():
    ttype = var_type.get()
    category = entry_category.get()
    amount = entry_amount.get()
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Ошибка", "Сумма должна быть числом.")
        return

    add_transaction(ttype, category, amount)
    messagebox.showinfo("Успех", f"{ttype.capitalize()} добавлена: {amount} руб, категория: {category}")

def on_stats():
    stats = get_statistics()
    messagebox.showinfo("Статистика", stats)

root = tk.Tk()
root.title("💰 pybudget GUI")

var_type = tk.StringVar(value="доход")

tk.Radiobutton(root, text="Доход", variable=var_type, value="доход").grid(row=0, column=0)
tk.Radiobutton(root, text="Расход", variable=var_type, value="расход").grid(row=0, column=1)

tk.Label(root, text="Категория").grid(row=1, column=0)
entry_category = tk.Entry(root)
entry_category.grid(row=1, column=1)

tk.Label(root, text="Сумма").grid(row=2, column=0)
entry_amount = tk.Entry(root)
entry_amount.grid(row=2, column=1)

tk.Button(root, text="Добавить", command=on_add).grid(row=3, column=0, columnspan=2, pady=5)
tk.Button(root, text="Статистика", command=on_stats).grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()

