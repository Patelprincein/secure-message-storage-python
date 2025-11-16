import hashlib
import os
import json
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

result_file = "encrypted_data.json"
key_size = 32

def create_key(password, hash_algo='sha256'):
    # creates the key from password using the selected hash algorithm and i trid to use sha256 as default one.
    hasher = hashlib.new(hash_algo)
    hasher.update(password.encode())
    return hasher.digest()

def encrypt_message(username, password, message, hash_algo):
    key = create_key(password, hash_algo) # uses create_key function and passes password and selected algo by user
    iv = get_random_bytes(AES.block_size) # generate random iv 
    cipher = AES.new(key, AES.MODE_CBC, iv) # create new aes object
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size)) # message converted to bytes

    hasher = hashlib.new(hash_algo) # creates new hash obeject 
    hasher.update(ciphertext) # put ciphertext in hash function
    integrity_hash = hasher.hexdigest() # convert to readable hexadecimal string

    data_to_save = []   # empaty list so if files exists and have any data it will take it out to this list and then append this list and then save data back to the file by over writing it.
    if os.path.exists(result_file):
        with open(result_file, 'r') as f:
            try:
                data_to_save = json.load(f)
            except json.JSONDecodeError:
                data_to_save = []

    new_data = {   #new object is created to add in file
        "user_id": username,
        "iv": base64.b64encode(iv).decode(),
        "ciphertext": base64.b64encode(ciphertext).decode(),
        "integrity_hash": integrity_hash,
        "hash_algo": hash_algo
    }

    data_to_save.append(new_data)  # add neq data object to list

    with open(result_file, 'w') as f:   # overwrite the file with added new object in data_to_save
        json.dump(data_to_save, f, indent=2)

    print("\nMessage encrypted and stored successfully!")

def decrypt_message(username, password):
    if not os.path.exists(result_file): #if file not exist or not there it returns this
        print("No encrypted file found.")
        return

    with open(result_file, 'r') as f:
        try:
            all_data = json.load(f)
        except json.JSONDecodeError:    # checks if it have any error then returns this!
            print("File is corrupted.")
            return

    found = False
    for data in all_data:
        if data.get("user_id") == username:     # takes out data from the file and based on username
            found = True
            hash_algo = data.get("hash_algo")
            key = create_key(password, hash_algo)
            iv = base64.b64decode(data["iv"])
            ciphertext = base64.b64decode(data["ciphertext"])
            stored_hash = data["integrity_hash"]

            check_hash = hashlib.new(hash_algo)
            check_hash.update(ciphertext)
            new_hash = check_hash.hexdigest()

            if new_hash != stored_hash:     # calculated new hash check with the stored one.
                print("Message tampering detected! Decryption skipped.")
                continue
            try:
                cipher = AES.new(key, AES.MODE_CBC, iv) # creates new aes object for decription
                decrypted_padded = cipher.decrypt(ciphertext)   # do the drcription
                plaintext = unpad(decrypted_padded, AES.block_size).decode() # remove the padding
                print(f"\nDecrypted message for {username}: {plaintext}")
            except Exception:
                print("Wrong password or data corrupted.")

    if not found:
        print("No messages found for this user.")

def main():
    print("AES Encryption and Decryption Program.")

    while True:
        print("\n1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = input("Choose option (1/2/3): ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            message = input("Enter your message: ")

            algo_choice = input("Choose hash algorithm (a for sha256, b for md5): ").lower()
            hash_algo = 'md5' if algo_choice == 'b' else 'sha256'

            encrypt_message(username, password, message, hash_algo)

        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            decrypt_message(username, password)

        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()