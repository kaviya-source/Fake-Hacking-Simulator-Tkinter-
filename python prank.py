import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("System Security Scanner")
root.geometry("500x250")

label = tk.Label(
    root,
    text="Scanning your computer for critical threats...",
    font=("Arial", 14)
)
label.pack(pady=20)

progress = tk.Label(root, text="0%", font=("Arial", 24))
progress.pack()

def update_progress(i=0):
    if i <= 100:
        progress.config(text=f"{i}%")
        root.after(50, update_progress, i + 1)
    else:
        messagebox.showwarning(
            "Critical Alert",
            "⚠️ 9,482 viruses detected!\nImmediate action required!"
        )
        root.after(2000, reveal_prank)

def reveal_prank():
    messagebox.showinfo(
        "😂 Prank!",
        "Relax! This was just a harmless prank.\nYour computer is fine!"
    )
    root.destroy()

update_progress()

root.mainloop()
