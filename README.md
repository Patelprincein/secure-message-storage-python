\# CS2413 – Cryptography Assignment 1



This repository contains my solutions for Assignment 1 from the course CS2413 (Information Security).  

All three questions are included in one place so anyone can run and learn from them.  

Professor-provided files are also included.



---



\## Files in this Repository



encryption\_system.py  

hash\_checker.py  

rsa\_decryption.py  



private\_key.pem  

encrypted\_message.txt  



Programming\_Assignment-1-Report.docx  



requirements.txt  

README.md  



---



\## Question 1 – AES Message Storage



This program allows a user to store secret messages securely.



It does the following:



\- Creates an encryption key from the user’s password (SHA-256 or MD5)  

\- Encrypts the message using AES in CBC mode  

\- Uses a random IV for every encryption  

\- Saves encrypted data into a JSON file  

\- Adds a hash of the ciphertext to detect tampering  

\- Allows the user to decrypt their message later  



To run:

python  encryption\_system.py



---



\## Question 2 – SHA-256 Hash Checker



This program reads the file private\_key.pem and calculates its SHA-256 hash.  

It compares this hash to four multiple-choice options and prints which one matches.



To run:



python hash\_checker.py

---



\## Question 3 – RSA OAEP Decryption



This program decrypts a Base64-encoded encrypted message using the professor’s private key.



It does the following:



\- Loads private\_key.pem  

\- Reads encrypted\_message.txt  

\- Decodes the Base64 ciphertext  

\- Decrypts it using RSA with OAEP padding  

\- Prints the decrypted message  



To run:



python rsa\_decryption.py

---



\## Included Professor Files



private\_key.pem  

encrypted\_message.txt  

Programming\_Assignment-1-Report.docx  



These files are included so that anyone can run the programs exactly like in the assignment.



---



\## Installation



Install required libraries:



pip install -r requirements.txt



---



\## What I Learned



\- AES encryption (CBC mode)  

\- RSA OAEP decryption  

\- Hash functions (SHA-256, MD5)  

\- Password-based key generation  

\- How to check integrity with hashes  

\- How to read and write files in Python  

\- How to work with JSON and Base64  

\- How real encryption systems store data  



---



\## Author



Prince Patel  

University of New Brunswick  

CS2413 – Information Security



