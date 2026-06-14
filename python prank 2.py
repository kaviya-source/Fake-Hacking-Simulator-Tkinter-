import tkinter as tk
import random

root = tk.Tk()
root.title("Elite Hacker Terminal")
root.geometry("700x450")
root.configure(bg="black")

terminal = tk.Text(
    root,
    bg="black",
    fg="lime",
    font=("Consolas", 11),
    insertbackground="lime"
)
terminal.pack(fill="both", expand=True)

messages = [
    "Initializing secure connection...",
    "Locating encrypted database...",
    "Bypassing firewall...",
    "Decrypting passwords...",
    "Downloading classified files...",
    "Accessing satellite network...",
    "Injecting AI module...",
    "Finalizing operation..."
]

def type_line(text, index=0):
    if index < len(text):
        terminal.insert("end", text[index])
        terminal.see("end")
        root.after(25, type_line, text, index + 1)
    else:
        terminal.insert("end", "\n")
        next_step()

step = 0

def next_step():
    global step
    if step < len(messages):
        delay = random.randint(500, 1200)
        msg = messages[step]
        step += 1
        root.after(delay, lambda: type_line(msg))
    else:
        root.after(1000, reveal)

def reveal():
    terminal.insert("end", "\n")
    terminal.insert("end", "####################################\n")
    terminal.insert("end", "#      SYSTEM SUCCESSFULLY HACKED  #\n")
    terminal.insert("end", "####################################\n\n")
    terminal.insert("end", "😂 JUST KIDDING!\n")
    terminal.insert("end", "This was a harmless prank.\n")
    terminal.see("end")

next_step()

root.mainloop()
