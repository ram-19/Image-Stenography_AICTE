# Image-Stenography_AICTE

# 🔐 Image Encryption & Decryption Using AES & Steganography  

This project encrypts a secret message using **AES (CBC Mode)** and hides it inside an image using **steganography**. The encrypted image can then be decrypted using the correct passcode to retrieve the original message.  

## 🚀 Features  
✅ **AES-256 Encryption (CBC Mode)** – Secure message encryption with a passcode.  
✅ **Steganography** – Hides encrypted data within an image's pixel values.  
✅ **Modern GUI with Light/Dark Mode** – Easy-to-use Tkinter-based interface.  
✅ **File Selection Preview** – Displays the selected image name instead of the full path.  
✅ **Decryption with Passcode Protection** – Only the correct passcode retrieves the hidden message.  
✅ **Cross-Platform Compatibility** – Works on Windows, macOS, and Linux.  


## 🛠️ Setup Instructions  

### 1️⃣ Prerequisites  
Ensure you have **Python 3.10+** installed along with the required dependencies.  

Install dependencies using:  
bash --> pip install opencv-python cryptography pycryptodome

### 2️⃣ Clone the Repository  
     
     --> git clone https://github.com/ram-19/Image-Stenography_AICTE.git

     --> cd Image-Stenography_AICTE

### 3️⃣ Run the Encryption Tool  
bash --> python encrypt_gui.py

#### **Steps:**  
1️⃣ Select an image (**.png / .jpg / .jpeg**).  
2️⃣ Enter the secret message.  
3️⃣ Set a passcode for encryption.  
4️⃣ Click **"Encrypt"**, and a new encrypted image will be generated.  

🔹 **Example Output:**  

✅ Encryption Successful!  
New Image: example_encrypted.png

### 4️⃣ Run the Decryption Tool  
bash --> python decrypt_gui.py

#### **Steps:**  
1️⃣ Select the encrypted image.  
2️⃣ Enter the correct passcode.  
3️⃣ Click **"Decrypt"** to retrieve the hidden message.  

🔹 **Example Output:**  

🔓 Decryption Successful!  
Secret Message: "Hello, this is a secret!"

## 🎨 GUI Features  
  **Light/Dark Mode** 🌙 – Toggle between themes for a better user experience.  
  **Status Updates** 📢 – Displays encryption/decryption progress messages inside the window.  
  **File Preview** 🖼️ – Shows the selected image name before encryption/decryption.  

## 📂 File Structure  

  📁 Image-Stenography_AICTE
  │── encrypt_gui.py        # GUI for encryption
  │── decrypt_gui.py        # GUI for decryption
  │── README.md             # Documentation

## 🛡️ Security Notes  
   **Only images are modified** – No separate text files or metadata changes.  
   **AES-256 CBC Mode** ensures strong encryption.  
   **Without the correct passcode, decryption is impossible**.  

## 🤝 Contribution  
Pull requests are welcome! Open an issue if you find bugs or need improvements.  

## 📜 License  
MIT License. Free for personal and commercial use.  

## ⭐ Show Support  
If you find this project useful, give it a ⭐ on GitHub!  

## 📧 Contact  
For issues or suggestions, reach out via GitHub Issues or Email: ramprabhathsirimalla6@gmail.com  
