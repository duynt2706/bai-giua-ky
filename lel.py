import tkinter as tk

def encrypt_decrypt():
    text = input_text.get("1.0", "end-1c")  # Get text from input field
    key = int(key_entry.get())

    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if mode.get() == "enc":  # Encryption mode
                num = ord(char.lower()) - 97
                new_num = (num + key) % 26
                new_char = chr(new_num + 97)
            else:  # Decryption mode
                num = ord(char.lower()) - 97
                new_num = (num - key) % 26
                new_char = chr(new_num + 97)
            encrypted_text += new_char
        else:
            encrypted_text += char

    output_text.delete("1.0", "end")  # Clear output field
    output_text.insert("1.0", encrypted_text)  # Display result

window = tk.Tk()
window.title("Caesar Cipher")

label_title = tk.Label(window, text="Caesar Cipher")
label_title.pack()

frame = tk.Frame(window)
frame.pack()

# Input text field
input_text = tk.Text(frame, height=5, width=30)
input_text.pack(side=tk.LEFT)

# Encryption/Decryption mode radio buttons
mode = tk.StringVar(value="enc")  # Start with encryption mode
radio_enc = tk.Radiobutton(frame, text="Encrypt", variable=mode, value="enc")
radio_dec = tk.Radiobutton(frame, text="Decrypt", variable=mode, value="dec")
radio_enc.pack()
radio_dec.pack()

# Key entry
key_label = tk.Label(frame, text="Key:")
key_label.pack(side=tk.LEFT)
key_entry = tk.Entry(frame, width=5)
key_entry.pack(side=tk.LEFT)

# Cipher/Decipher button
button = tk.Button(frame, text="Cipher/Decipher", command=encrypt_decrypt)
button.pack()

# Output text field
output_text = tk.Text(window, height=5, width=40)
output_text.pack()

window.mainloop()
