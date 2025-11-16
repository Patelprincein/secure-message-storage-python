### **CS2413 -- CRYPTOGRAPHY ASSIGNMENT 1: INFORMATION SECURITY**



**========================================================**



This repository contains my completed solutions for Programming Assignment 1 from the course CS2413 (Information Security) at the University of New Brunswick.



The project demonstrates practical applications of the following core concepts:



**Symmetric Encryption (AES)**



**Asymmetric Decryption (RSA)**



**Cryptographic Hashing (SHA-256, MD5)**



All three assignments are implemented in Python. Professor-provided resource files are included to ensure immediate execution and verification.



**========================================================**



##### **REPOSITORY CONTENTS AND SETUP:**



###### The files are structured as follows:



**encryption\_system.py (Solution Code):** Solution for Question 1 (AES Message Storage).

**hash\_checker.py (Solution Code):** Solution for Question 2 (SHA-256 Hash Check).

**rsa\_decryption.py (Solution Code):** Solution for Question 3 (RSA OAEP Decryption).

**requirements.txt (Configuration):** Python dependencies required to run the solutions.

**private\_key.pem (Resource):** Professor-provided RSA private key file.

**encrypted\_message.txt (Resource):** Professor-provided Base64 ciphertext.

**Programming\_Assignment-1-Report.docx (Documentation): The formal assignment.**



**========================================================**



##### **Installation Instructions:**



To run the programs locally, you must install the required Python libraries:



pip install -r requirements.txt





**========================================================**



##### **ASSIGNMENT SOLUTIONS OVERVIEW**



**Question 1:** **AES Message Storage (encryption\_system.py)**



This program simulates a secure message storage system. Key generation from a user's password using SHA-256 or MD5. Encryption using AES in CBC mode. Use of a random Initialization Vector (IV) for every encryption. Data integrity check by adding a hash of the ciphertext upon saving. Decryption function to recover the message using the original password.



**To Run:**

python encryption\_system.py



**========================================================**



**Question 2: SHA-256 Hash Checker (hash\_checker.py)**

This utility verifies the integrity of a critical resource file. Reads the private\_key.pem file. Calculates the SHA-256 hash of the file's contents. Compares the result to multiple-choice options for authenticity confirmation.



**To Run:**

python python hash\_checker.py



**========================================================**



**Question 3: RSA OAEP Decryption (rsa\_decryption.py):**

This program demonstrates the use of asymmetric cryptography for message recovery. Loads the private key from private\_key.pem. Reads the Base64-encoded ciphertext from encrypted\_message.txt. Performs decryption using RSA with Optimal Asymmetric Encryption Padding (OAEP). Prints the successfully decrypted message.



**To Run:**

python rsa\_decryption.py



**========================================================**



##### **KEY LEARNING OUTCOMES**

This assignment provided hands-on experience with: AES symmetric encryption (CBC mode). RSA OAEP asymmetric decryption. Implementing Hash Functions (SHA-256, MD5) for integrity. Secure methods for Password-Based Key Derivation. Working with data encoding formats: JSON and Base64. Understanding encryption data storage structure.



**========================================================**



##### **AUTHOR \& COURSE INFORMATION**



Author: **Prince Patel**

Course: CS2413 – Information Security

Institution: University of New Brunswick

