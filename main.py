import tkinter as tk
from tkinter import messagebox
import config
import utils

def send_message():
    user_input = entry.get()
    if not user_input.strip():
        return
    chat_history.insert(tk.END, f"You: {user_input}")
    
    if config.API_KEY == "YOUR_API_KEY_HERE":
        bot_response = "Hello! This is a placeholder response. Replace API_KEY in config.py to enable real responses."
    else:
        bot_response = f"Bot [API_KEY active]: You said '{user_input}'"
    
    chat_history.insert(tk.END, f"Bot: {bot_response}")
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Coffee Beans Chatbot")
chat_history = tk.Listbox(root, width=80, height=20)
chat_history.pack(padx=10, pady=10)

entry = tk.Entry(root, width=60)
entry.pack(side=tk.LEFT, padx=(10,0), pady=(0,10))
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.LEFT, padx=(5,10), pady=(0,10))

root.mainloop()
