import tkinter as tk
from tkinter import messagebox
from pyDes import des, PAD_PKCS5
import binascii

def des_encrypt(message, key):
    # Convert the key from hex string to bytes
    key = binascii.unhexlify(key)
    # Create a DES object with the specified key
    k = des(key, PAD_PKCS5)
    # Encrypt the message
    ciphertext = k.encrypt(message)
    return binascii.hexlify(ciphertext).decode()

def encrypt_message():
    message = entry_message.get().strip()
    key = entry_key.get().strip()
    num_rounds = int(entry_rounds.get())

    if len(message) != 16 or len(key) != 16:
        messagebox.showerror("Error", "Message and key should be 16 bytes (32 characters) in hexadecimal.")
        return

    # Perform DES encryption for specified number of rounds
    ciphertext = message
    for i in range(num_rounds):
        ciphertext = des_encrypt(binascii.unhexlify(ciphertext), key)  # Don't convert the key here
        text_output.insert(tk.END, f"Round {i+1}: Ciphertext: {ciphertext}\n")

# Create the main window
root = tk.Tk()
root.title("DES Encryption")

# Create input fields
label_message = tk.Label(root, text="Enter message to encrypt:")
label_message.grid(row=0, column=0, padx=10, pady=5)
entry_message = tk.Entry(root)
entry_message.grid(row=0, column=1, padx=10, pady=5)

label_key = tk.Label(root, text="Enter encryption key:")
label_key.grid(row=1, column=0, padx=10, pady=5)
entry_key = tk.Entry(root)
entry_key.grid(row=1, column=1, padx=10, pady=5)

label_rounds = tk.Label(root, text="Enter number of rounds:")
label_rounds.grid(row=2, column=0, padx=10, pady=5)
entry_rounds = tk.Entry(root)
entry_rounds.grid(row=2, column=1, padx=10, pady=5)

# Create encrypt button
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_message)
encrypt_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Create output text box
text_output = tk.Text(root, width=50, height=25)
text_output.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Run the main event loop
root.mainloop()
