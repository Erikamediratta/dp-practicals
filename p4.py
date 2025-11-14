import hashlib  

def hash_password(password):  
    password_bytes = password.encode()  
    hash_object = hashlib.sha256(password_bytes)  
    hex_digest = hash_object.hexdigest()  
    return hex_digest 

user_input = input("Enter a password: ")  
hashed = hash_password(user_input)  
print("SHA-256 hash:", hashed)  
