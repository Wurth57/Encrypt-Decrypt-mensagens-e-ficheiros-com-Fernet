from cryptography.fernet import Fernet

def load_key():
    """Load the shared key from key.key"""
    return open("key.key", "rb").read()

def decrypt_message():
    key = load_key()
    f = Fernet(key)

    # Lê a mensagem encriptada do ficheiro
    with open("encrypted_message.txt", "rb") as file:
        encrypted = file.read()

    # Desencripta
    decrypted = f.decrypt(encrypted)

    # Mostra a mensagem original
    print("🗝️ Mensagem desencriptada:", decrypted.decode())

if __name__ == "__main__":
    decrypt_message()
