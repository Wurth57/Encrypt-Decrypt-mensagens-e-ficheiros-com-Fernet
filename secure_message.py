from cryptography.fernet import Fernet
import os

def write_key():
    """Generate and save a key into key.key"""
    key = Fernet.generate_key()
    key_path = os.path.abspath("key.key")
    print("🔐 Saving key to:", key_path)
    with open(key_path, "wb") as key_file:
        key_file.write(key)

def load_key():
    """Load the key from key.key"""
    return open("key.key", "rb").read()

# ==== Basic Test ====
if __name__ == "__main__":
    write_key()
    key = load_key()
    print("🔑 Shared Key:", key.decode())

    # Pede mensagem ao utilizador
    plaintext = input("\n📝 Escreve uma mensagem para encriptar: ").encode()

    # Inicializa o Fernet
    f = Fernet(key)

    # Encripta a mensagem
    encrypted = f.encrypt(plaintext)
    print("🔒 Mensagem encriptada:", encrypted.decode())

    # Guarda num ficheiro
    with open("encrypted_message.txt", "wb") as file:
        file.write(encrypted)
    print("💾 Mensagem guardada em 'encrypted_message.txt'")
