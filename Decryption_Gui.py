import cv2
import os
import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

LIGHT_THEME = {"bg": "#f4f4f4", "fg": "#000000", "btn_bg": "#0078D7", "btn_fg": "#ffffff"}
DARK_THEME = {"bg": "#2e2e2e", "fg": "#ffffff", "btn_bg": "#005a9e", "btn_fg": "#ffffff"}

dark_mode = False

def decrypt_message(encrypted_bytes, passcode):
    """ Decrypts the message using AES (CBC Mode) """
    key = hashlib.sha256(passcode.encode()).digest()
    iv = encrypted_bytes[:16]
    ciphertext = encrypted_bytes[16:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_bytes = unpad(cipher.decrypt(ciphertext), AES.block_size)

    return decrypted_bytes.decode('utf-8')

def browse_image():
    """ Browse for an encrypted image file """
    file_path = filedialog.askopenfilename(title="Select Encrypted Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        filename = os.path.basename(file_path)
        entry_image.delete(0, tk.END)
        entry_image.insert(0, filename)
        entry_image.path = file_path

def decode_message():
    """ Extract and decrypt message from image """
    if not hasattr(entry_image, 'path'):
        messagebox.showerror("Error", "Please select an encrypted image!")
        return

    image_path = entry_image.path
    passcode = entry_passcode.get()

    if not passcode:
        messagebox.showerror("Error", "Passcode is required!")
        return

    img = cv2.imread(image_path)
    if img is None:
        messagebox.showerror("Error", "Image not found!")
        return

    message_length = sum(img[0, i, 0] << (8 * i) for i in range(4))

    encrypted_bytes = bytearray()
    idx = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if i == 0 and j < 4:
                continue
            for k in range(3):
                if idx < message_length:
                    encrypted_bytes.append(img[i, j, k])
                    idx += 1
                else:
                    break
            if idx >= message_length:
                break
        if idx >= message_length:
            break

    try:
        decrypted_message = decrypt_message(encrypted_bytes, passcode)
        messagebox.showinfo("Decryption Successful", f"🔓 Decrypted Message:\n{decrypted_message}")
    except Exception:
        messagebox.showerror("Error", "Decryption failed: Incorrect passcode or corrupted image!")

def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    theme = DARK_THEME if dark_mode else LIGHT_THEME

    root.configure(bg=theme["bg"])
    for widget in root.winfo_children():
        widget.configure(bg=theme["bg"], fg=theme["fg"])

root = tk.Tk()
root.title("Image Decryption")
root.geometry("400x250")

tk.Label(root, text="Select Encrypted Image:").pack()
entry_image = tk.Entry(root, width=40)
entry_image.pack()
tk.Button(root, text="Browse", command=browse_image).pack()

tk.Label(root, text="Enter Passcode:").pack()
entry_passcode = tk.Entry(width=40, show="*")
entry_passcode.pack()

tk.Button(root, text="Decrypt", command=decode_message).pack()
tk.Button(root, text="Toggle Dark Mode", command=toggle_dark_mode).pack()

root.mainloop()
