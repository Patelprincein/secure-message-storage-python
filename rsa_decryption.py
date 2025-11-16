import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

with open("private_key.pem", "rb") as file:     # read the file and imports the key
    private_key = RSA.import_key(file.read())

with open("encrypted_message.txt", "rb") as file:   # read the file and add text in cipher_text varible
    cipher_text = file.read()

cipher_bytes = base64.b64decode(cipher_text)    # decode the message
cipher = PKCS1_OAEP.new(private_key)            # create rsa oaep object to help decrypt the message
decrypted_message = cipher.decrypt(cipher_bytes) #  decrypts the ciphertext bytes

print("Decrypted message:")
print(decrypted_message.decode())