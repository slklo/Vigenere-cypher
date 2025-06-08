## Vigenere-cypher

A simple implementation of the **Vigenère Cipher**, a method of encrypting **alphabetic text** using a keyword to create a **polyalphabetic** substitution cipher.

The **Vigenère Cipher** is a classical **encryption algorithm** that uses a keyword to **shift letters in the plaintext**, producing ciphertext that is more secure than a **simple Caesar cipher**. This project demonstrates how the **Vigenere Cipher works** and provides a way to **encrypt and decrypt** text using a chosen keyword.

Features: Encrypt your text in 3 possible ways (English only, Russian only, or English + Russian + symbols), decrypt text back to the original, supports both uppercase and lowercase characters, simple and interactive CLI.

#### Technologies used: Python, Tkinter. 

#### Encryption process using the Vigenère Cipher: 

Example text: hello

Example key: key 

1. Matching the lengths: (hello: keyke)

2. Converts letters to numbers, depending on their alphabetic index. (h - 7, e - 4, l - 11, l - 11, o - 14) and (k - 10, e - 4, y - 24, k - 10, e - 4)

3. Using the encryption formula ((text + key) mod length of alphabet), we are encrypt the text.

   Example: (7 + 10) % 26  = 17 -> r, (4 + 4) % 26 = 8 -> i and so on.
   
4. Finally, we get the encrypted text: RIJVS

#### The decryption of the text: 

Example encrypted: rijvs
Example key: key

1. Matching the lengths: (rijvs: keyke)

2. Converts letters to numbers (r - 17, i - 8) and so on

3. Using the decryption formula: ((encrypted text - key + length of alphabet) mod length of alphabet)

4. In the end we get the result: hello

Wiki link for vigenere cypher - https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher

Feel free to reach out for questions or suggestions!

