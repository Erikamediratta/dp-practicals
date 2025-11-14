def encrypt_caesar(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted += new_char
        else:
            encrypted += char
    return encrypted


def decrypt_caesar(text, shift):
    return encrypt_caesar(text, -shift)



message = input("Enter a message: ")
shift_value = int(input("Enter shift number: "))

encrypted_message = encrypt_caesar(message, shift_value)
print("Encrypted:", encrypted_message)

decrypted_message = decrypt_caesar(encrypted_message, shift_value)
print("Decrypted:", decrypted_message)
