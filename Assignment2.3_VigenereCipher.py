# Zemerelin Iris M. Membrere
# BSCPE 1-4
# Assignment 2

# Problem 3 - The Vigenere Cipher

# Define function to generate keyword
def Keyword(message, key):
    key = list(key)
# If the length of the message == key, return key
    if len(message) == len(key):
        return key
# If not, append the key
    else:
        for i in range (len(message) - len(key)):
            key.append(key[i % len(key)])
        return ("".join(key))