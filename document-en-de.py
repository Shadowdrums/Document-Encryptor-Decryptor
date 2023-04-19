import os
from cryptography.fernet import Fernet

def get_files(path):
    """
    Recursively search the specified directory and its subdirectories
    for files and return a list of their paths.
    """
    file_paths = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

def generate_key():
    """
    Generate a new encryption key and save it to a file.
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    """
    Load the encryption key from the key file.
    """
    try:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
        return key
    except FileNotFoundError:
        print("Key file not found. Generating new key.")
        return generate_key()

def encrypt_file(file_path, key):
    """
    Encrypt the specified file using the provided encryption key.
    """
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)
        with open(file_path, 'wb') as f:
            f.write(encrypted)
        print(f"{file_path} encrypted successfully.")
    except Exception as e:
        print(f"Error encrypting {file_path}: {e}")

def decrypt_file(file_path, key):
    """
    Decrypt the specified file using the provided encryption key.
    """
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        fernet = Fernet(key)
        decrypted = fernet.decrypt(data)
        with open(file_path, 'wb') as f:
            f.write(decrypted)
        print(f"{file_path} decrypted successfully.")
    except Exception as e:
        print(f"Error decrypting {file_path}: {e}")

def main():
    # Load the encryption key
    key = load_key()

    # Search for files in the current directory and its subdirectories
    file_paths = get_files(os.getcwd())

    # Display a list of files and ask the user which one to encrypt/decrypt
    print("Files:")
    for i, file_path in enumerate(file_paths):
        print(f"{i}: {file_path}")
    try:
        choice = int(input("Enter file number: "))
        file_path = file_paths[choice]
    except (ValueError, IndexError):
        print("Invalid file number.")
        return

    # Encrypt or decrypt the chosen file
    action = input("Encrypt or decrypt? ").lower()
    if action == "encrypt":
        encrypt_file(file_path, key)
    elif action == "decrypt":
        decrypt_file(file_path, key)
    else:
        print("Invalid action.")

if __name__ == "__main__":
    main()
