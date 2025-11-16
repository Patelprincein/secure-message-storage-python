import hashlib

filePath = "private_key.pem"

given_hashes = {
    "A": "1a4c8b9d847b3e2fa2d5f9d31c8e5f8b7c91a5d0f4e5b2f7d8c6e2a9b4d5e1c3",
    "B": "9e427f6bea8af1fc9d2d332312338cf538759ebe5f71843af205c18d726623f9",
    "C": "3f4b5c2d9a8e7f1c5d3b2a9c6e1d4f7b8a2c5e9f1d0b3a7c8e6d2f5b9a4c3e1d",
    "D": "0d09a513353e632b068a1a49e6ecc0b2c753ccc1c95cb1751745ba576d1396c8"
}

try:
    with open(filePath, "rb") as file:      #opens the file read data in data varible
        data = file.read()

    sha_hash = hashlib.sha256(data).hexdigest() #uses hashlib and compute sha hash on data and save it in sha_hash
    for option, hash_value in given_hashes.items():
        if sha_hash == hash_value:      # check if matches the hash
            print(f"Success! The hash matches option {option}.")
            break
    else:
        print("No match found among the provided options.")

except FileNotFoundError:
    print(f" Error: '{filePath}' not found. Make sure the file is in the same folder.")