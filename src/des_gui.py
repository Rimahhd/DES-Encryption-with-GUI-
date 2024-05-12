import tkinter as tk
import binascii
from tkinter import messagebox
from pyDes import des, PAD_PKCS5


def des_encrypt(message, key):
    # Convert key from hex string to byte
    key = binascii.unhexlify(key)
    # Create a DES object with the specified key
    sKey = des(key, PAD_PKCS5)
    # Encrypt the msg.
    ciphertext = sKey.encrypt(message)
    return binascii.hexlify(ciphertext).decode()

def encrypt_message():
    message = entryMessage.get().strip()
    key = entryKey.get().strip()

    if len(message) != 16 or len(key) != 16:
        messagebox.showerror("Error", "Message and key should be 16 bytes (32 characters).")
        return

    # Perform DES encryption for specified number of rounds
    ciphertext = message
    ciphertext = des_encrypt(binascii.unhexlify(ciphertext), key)  
    text_output.insert(tk.END, f"Ciphertext: {ciphertext}\n")

# Create the main window
root = tk.Tk()
root.title("DES Encryption RIMAHHD")

# Create input fields
labelMessage = tk.Label(root, text="Enter your message to encrypt:")
labelMessage.grid(row=0, column=0, padx=10, pady=5)
entryMessage = tk.Entry(root)
entryMessage.grid(row=0, column=1, padx=10, pady=5)

labelKey = tk.Label(root, text="Enter the encryption key:")
labelKey.grid(row=1, column=0, padx=10, pady=5)
entryKey = tk.Entry(root)
entryKey.grid(row=1, column=1, padx=10, pady=5)


# Create encrypt button
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_message)
encrypt_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Create output text box
text_output = tk.Text(root, width=50, height=25)
text_output.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Run the main event loop
root.mainloop()
