import tkinter as tk
from tkinter import messagebox
import requests

def send_message():
    webhook_url = webhook_url_entry.get()
    message = message_entry.get("1.0", tk.END).strip()
    
    if not webhook_url or not message:
        messagebox.showerror("Error", "Webhook URL and message cannot be empty")
        return
    
    data = {
        "content": message
    }
    
    response = requests.post(webhook_url, json=data)
    
    if response.status_code == 204:
        messagebox.showinfo("Success", "Message sent successfully")
    else:
        messagebox.showerror("Error", f"Failed to send message. Status code: {response.status_code}")

# Create the main application window
root = tk.Tk()
root.title("Discord Webhook Sender")

# Webhook URL input
tk.Label(root, text="Webhook URL:").grid(row=0, column=0, padx=10, pady=10)
webhook_url_entry = tk.Entry(root, width=50)
webhook_url_entry.grid(row=0, column=1, padx=10, pady=10)

# Message input
tk.Label(root, text="Message:").grid(row=1, column=0, padx=10, pady=10)
message_entry = tk.Text(root, width=50, height=10)
message_entry.grid(row=1, column=1, padx=10, pady=10)

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()