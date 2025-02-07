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

def send_embed():
    webhook_url = webhook_url_entry.get()
    embed_title = embed_title_entry.get()
    embed_description = embed_description_entry.get("1.0", tk.END).strip()
    embed_color = embed_color_entry.get()
    embed_url = embed_url_entry.get()
    embed_footer = embed_footer_entry.get()
    
    if not webhook_url or not embed_title or not embed_description or not embed_color:
        messagebox.showerror("Error", "All embed fields must be filled")
        return
    
    try:
        embed_color = int(embed_color, 16)
    except ValueError:
        messagebox.showerror("Error", "Embed color must be a valid hex code")
        return
    
    embed = {
        "title": embed_title,
        "description": embed_description,
        "color": embed_color
    }
    
    if embed_url:
        embed["url"] = embed_url
    
    if embed_footer:
        embed["footer"] = {"text": embed_footer}
    
    data = {
        "embeds": [embed]
    }
    
    response = requests.post(webhook_url, json=data)
    
    if response.status_code == 204:
        messagebox.showinfo("Success", "Embed sent successfully")
    else:
        messagebox.showerror("Error", f"Failed to send embed. Status code: {response.status_code}")

# Create the main application window
root = tk.Tk()
root.title("Discord Webhook Sender")

# Webhook URL input
tk.Label(root, text="Webhook URL:").grid(row=0, column=0, padx=10, pady=10)
webhook_url_entry = tk.Entry(root, width=50)
webhook_url_entry.grid(row=0, column=1, padx=10, pady=10)

# Message input
tk.Label(root, text="Message:").grid(row=1, column=0, padx=10, pady=10)
message_entry = tk.Text(root, width=50, height=5)
message_entry.grid(row=1, column=1, padx=10, pady=10)

# Send message button
send_button = tk.Button(root, text="Send Message", command=send_message)
send_button.grid(row=2, column=0, columnspan=2, pady=10)

# Embed title input
tk.Label(root, text="Embed Title:").grid(row=3, column=0, padx=10, pady=10)
embed_title_entry = tk.Entry(root, width=50)
embed_title_entry.grid(row=3, column=1, padx=10, pady=10)

# Embed description input
tk.Label(root, text="Embed Description:").grid(row=4, column=0, padx=10, pady=10)
embed_description_entry = tk.Text(root, width=50, height=5)
embed_description_entry.grid(row=4, column=1, padx=10, pady=10)

# Embed color input
tk.Label(root, text="Embed Color (hex):").grid(row=5, column=0, padx=10, pady=10)
embed_color_entry = tk.Entry(root, width=50)
embed_color_entry.grid(row=5, column=1, padx=10, pady=10)

# Embed URL input
tk.Label(root, text="Embed Title URL (optional):").grid(row=6, column=0, padx=10, pady=10)
embed_url_entry = tk.Entry(root, width=50)
embed_url_entry.grid(row=6, column=1, padx=10, pady=10)

# Embed footer input
tk.Label(root, text="Embed Footer (optional):").grid(row=7, column=0, padx=10, pady=10)
embed_footer_entry = tk.Entry(root, width=50)
embed_footer_entry.grid(row=7, column=1, padx=10, pady=10)

# Send embed button
send_embed_button = tk.Button(root, text="Send Embed", command=send_embed)
send_embed_button.grid(row=8, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()