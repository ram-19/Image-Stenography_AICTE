import cv2
import os
import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

LIGHT_THEME = {"bg": "#f4f4f4", "fg": "#000000", "btn_bg": "#0078D7", "btn_fg": "#ffffff"}
DARK_THEME = {"bg": "#2e2e2e", "fg": "#ffffff", "btn_bg": "#005a9e", "btn_fg": "#ffffff"}

dark_mode = False  # Global theme toggle

def encrypt_message(secret_message, passcode):
    """ Encrypts the message using AES (CBC Mode) """
    key = hashlib.sha256(passcode.encode()).digest()
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    padded_message = pad(secret_message.encode('utf-8'), AES.block_size)
    encrypted_bytes = cipher.encrypt(padded_message)

    return iv + encrypted_bytes

def browse_image():
    """ Browse for an image file """
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        filename = os.path.basename(file_path)
        entry_image.delete(0, tk.END)
        entry_image.insert(0, filename)
        entry_image.path = file_path  # Store full path separately

def save_encrypted_image(img, original_path):
    """ Save encrypted image with a modified filename """
    base_name, ext = os.path.splitext(original_path)
    new_image_path = f"{base_name}_encrypted{ext}"
    cv2.imwrite(new_image_path, img)
    return new_image_path

def encode_message():
    """ Embed the encrypted message into an image """
    if not hasattr(entry_image, 'path'):
        messagebox.showerror("Error", "Please select an image!")
        return

    image_path = entry_image.path
    secret_message = entry_message.get()
    passcode = entry_passcode.get()

    if not secret_message or not passcode:
        messagebox.showerror("Error", "All fields are required!")
        return

    img = cv2.imread(image_path)
    if img is None:
        messagebox.showerror("Error", "Image not found!")
        return

    encrypted_message = encrypt_message(secret_message, passcode)
    print(f"\n🔒 DEBUG: Encrypted message stored in image.")

    encrypted_bytes = encrypted_message
    message_length = len(encrypted_bytes)
    
    if message_length > img.shape[0] * img.shape[1] * 3 - 4:
        messagebox.showerror("Error", "Image is too small to store the message!")
        return

    for i in range(4):
        img[0, i, 0] = (message_length >> (8 * i)) & 0xFF

    idx = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if i == 0 and j < 4:
                continue
            for k in range(3):
                if idx < message_length:
                    img[i, j, k] = encrypted_bytes[idx]
                    idx += 1
                else:
                    break
            if idx >= message_length:
                break
        if idx >= message_length:
            break

    new_image_path = save_encrypted_image(img, image_path)
    messagebox.showinfo("Success", f"✅ Encryption Successful!\nNew Image: {os.path.basename(new_image_path)}")

def toggle_dark_mode():
    """ Switch between light and dark mode """
    global dark_mode
    dark_mode = not dark_mode
    theme = DARK_THEME if dark_mode else LIGHT_THEME

    root.configure(bg=theme["bg"])
    for widget in root.winfo_children():
        if isinstance(widget, (tk.Label, tk.Entry, tk.Button)):
            widget.configure(bg=theme["bg"], fg=theme["fg"])
        if isinstance(widget, tk.Button):
            widget.configure(bg=theme["btn_bg"], fg=theme["btn_fg"])

root = tk.Tk()
root.title("Image Encryption")
root.geometry("400x300")

tk.Label(root, text="Select Image:").pack()
entry_image = tk.Entry(root, width=40)
entry_image.pack()
tk.Button(root, text="Browse", command=browse_image).pack()

tk.Label(root, text="Enter Secret Message:").pack()
entry_message = tk.Entry(root, width=40)
entry_message.pack()

tk.Label(root, text="Enter Passcode:").pack()
entry_passcode = tk.Entry(width=40, show="*")
entry_passcode.pack()

tk.Button(root, text="Encrypt", command=encode_message).pack()
tk.Button(root, text="Toggle Dark Mode", command=toggle_dark_mode).pack()

root.mainloop()
