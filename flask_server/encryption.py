from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def get_fernet(key):
    return Fernet(key)

def encrypt_data(data, key):
    f = get_fernet(key)
    return f.encrypt(data.encode()).decode()

def decrypt_data(token, key):
    f = get_fernet(key)
    return f.decrypt(token.encode()).decode()
