CS2413 – Cryptography Assignment 1: Information Security

This repository contains my completed solutions for Programming Assignment 1 from the course CS2413 (Information Security).

The project demonstrates practical applications of symmetric encryption (AES), asymmetric decryption (RSA), and cryptographic hashing (SHA-256, MD5). All three assignments are implemented in Python, and professor-provided files are included for immediate execution and verification.

🚀 Repository Contents & Setup

Key Files

File Name

Description

Category

encryption_system.py

Solution for Question 1 (AES Encryption).

Solution

hash_checker.py

Solution for Question 2 (SHA-256 Hash Check).

Solution

rsa_decryption.py

Solution for Question 3 (RSA OAEP Decryption).

Solution

requirements.txt

Python dependencies required to run the solutions.

Config

private_key.pem

Professor-provided file (used in Q2 and Q3).

Resource

encrypted_message.txt

Professor-provided file (ciphertext for Q3).

Resource

Programming_Assignment-1-Report.docx

The formal assignment report.

Documentation

Installation

To run the programs, you must first install the required Python libraries:

pip install -r requirements.txt


💡 Assignment Solutions Overview

Question 1: AES Message Storage

This program, encryption_system.py, simulates a secure message storage system.

It performs the following cryptographic steps:

Generates an encryption key from the user's password using a cryptographic hash function (SHA-256 or MD5).

Encrypts the secret message using the Advanced Encryption Standard (AES) in Cipher Block Chaining (CBC) mode.

Ensures security by using a random Initialization Vector (IV) for every encryption.

Saves the encrypted message and IV into a JSON file.

Adds a hash of the ciphertext to the file to detect any unauthorized tampering (data integrity check).

Allows the user to decrypt their message later using their password.

To Run:

python encryption_system.py


Question 2: SHA-256 Hash Checker

The program, hash_checker.py, verifies the integrity of the provided private key file.

It reads the private_key.pem file.

Calculates the SHA-256 hash of its contents.

Compares the calculated hash against four hardcoded multiple-choice options.

Prints the matching option to confirm the file's authenticity.

To Run:

python hash_checker.py


Question 3: RSA OAEP Decryption

This program, rsa_decryption.py, uses asymmetric cryptography to recover a secret message.

It loads the private key from private_key.pem.

Reads the Base64-encoded ciphertext from encrypted_message.txt.

Decodes the Base64 ciphertext back into its binary form.

Decrypts the binary data using RSA with the recommended Optimal Asymmetric Encryption Padding (OAEP) scheme.

Prints the successfully decrypted original secret message.

To Run:

python rsa_decryption.py


📚 Key Learning Outcomes

This assignment provided hands-on experience with fundamental security concepts:

Deepened understanding of AES symmetric encryption (CBC mode).

Practical application of RSA OAEP asymmetric decryption.

Implementing and utilizing various Hash Functions (SHA-256, MD5) for integrity checking and key generation.

Developing secure techniques for Password-Based Key Derivation.

Working with common data encoding formats like JSON and Base64.

Gaining insight into how real-world encryption systems structure and store data securely.

🧑‍💻 Author & Course Information

Author: Prince Patel
Course: CS2413 – Information Security
Institution: University of New Brunswick