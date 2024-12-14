import tkinter as tk
from tkinter import messagebox
import pyttsx3

engine = pyttsx3.init()

def play_text():
    text = text_box.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Text box is empty! Please enter some text.")
        return
    engine.say(text)
    engine.runAndWait()

def reset_text():
    text_box.delete("1.0", tk.END)

def exit_app():
    root.destroy()

root = tk.Tk()
root.geometry("500x300")

label = tk.Label(root, text="Enter Your words", font=("Arial", 18))
label.pack(pady =10)

text_box = tk.Text(root, wrap=tk.WORD, height=10, font=("Arial", 10))
text_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

play_button = tk.Button(button_frame, text="Play", command=play_text, width=10, bg="green")
play_button.grid(row=0, column=0, padx=5)

reset_button = tk.Button(button_frame, text="Reset", command=reset_text, width=10, bg="grey")
reset_button.grid(row=0, column=1, padx=5)

exit_button = tk.Button(button_frame, text="Exit", command=exit_app, width=10, bg="Red")
exit_button.grid(row=0, column=2, padx=5)

root.mainloop()