🔐 Encrypt & Decrypt Messages and Files with Fernet

This project demonstrates how to securely **encrypt and decrypt messages and files** using **Python** and the **Fernet** module from the `cryptography` library.

## 📁 Folder Structure

lab6folder/
├── key.key # Shared symmetric key
├── secure_message.py # Script to generate key and encrypt messages
├── decrypt_message.py # Script to decrypt encrypted messages
└── encrypted_message.txt # File containing encrypted output

shell
Copiar
Editar

## 🚀 Getting Started

### 1. Install Requirements

```bash
pip install cryptography
2. Generate Key & Encrypt Message
Run secure_message.py to:

Generate a shared symmetric key (key.key)

Encrypt a sample message

Save the encrypted message into encrypted_message.txt

bash
Copiar
Editar
python secure_message.py
3. Decrypt Message
Run decrypt_message.py to:

Load the key.key

Read and decrypt the encrypted_message.txt

Print the original message

bash
Copiar
Editar
python decrypt_message.py
🧠 Discussion Questions
What are the risks of sharing encryption keys improperly?
If a key is intercepted or shared insecurely, an attacker could decrypt sensitive data. This breaks the confidentiality of encrypted communication.

How does symmetric encryption differ from asymmetric encryption?

Symmetric encryption uses the same key to encrypt and decrypt.

Asymmetric encryption uses a public key to encrypt and a private key to decrypt.

What would happen if an attacker intercepted the encrypted message or file?
Without the key, they would be unable to read the original content. However, if they also obtained the key, the data would be compromised.

✅ Future Improvements
Add encryption/decryption for any file type (.pdf, .jpg, etc.)

Secure key exchange mechanism

GUI or command-line interface
