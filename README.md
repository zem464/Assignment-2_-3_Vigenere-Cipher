# Assignment-2_-3_Vigenere-Cipher

**Built for :** Subject assignment for Object Oriented Programming.

  **Submitted to :** Prof. Danilo Madrigalejos 
  
  **A.Y :** 2022-2023

## About the Project
**THE VIGENERE CIPHER**

The task is to write a program that asks the user for the plaintext (all uppercase letters, no spaces) and the keyword (all uppercase letters) and produce the ciphertext using the Vigenère cipher. 

Give the output of your program for the following message and key:

   **_Message :_** THISISTHELASTTASKHOORDAY
   
   **_Key :_** KNIGHTS

## About the Program
**STEPS**

1. Define a function in order to create a keyword. This will look like this:

       def Keyword(message, key):
       
     
           key = list(key)

2. Make sure that the parameter are of the same length. If it is equal, return key. If not, append the key to add element to the key.

3. Define another function for encryption the message. This will look like this:

       def encryption(message, key):
       
     
          encrypt_message = []

4. Add modulo 26 to the message and key. This will help in encrypting and decrypting the message according to vigenere cipher.

5. Utilize a conditional statement ``name and __main__`` in asking the user for the input. This will contain the output to ask for the message and the keyword, the key that was defined earlier, and the encrypt function that was also defined earlier.

6. Print the encrypted message using ``print()``.

## Running the Program

1. Input the message all in uppercase and no spaces.

2. Input the keyword all in uppercase.

3. The program will run to print the corresponding ciphered text.

### Contact
Zemerelin Iris M. Membrere - _zemerelinmembrere@gmail.com_

**Project Link :** https://github.com/zem464/Assignment-2_-3_Vigenere-Cipher.git

<p align="right">(<a href="#readme-top">back to top</a>)</p>
