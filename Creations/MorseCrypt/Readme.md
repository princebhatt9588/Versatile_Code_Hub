# Morse Code Encryption and Decryption Program

This program demonstrates a simple implementation of Morse code encryption and decryption. It converts text messages into Morse code and vice versa using a predefined Morse code dictionary. The program includes two main functions: `encrypt` to convert text into Morse code, and `decrypt` to convert Morse code back into text.

## Morse Code Dictionary

The Morse code dictionary (`MORSE_CODE_DICT`) maps each character (both letters and numbers) to its corresponding Morse code representation. It includes common English letters, digits, and some punctuation marks.

## How to Use the Program

1. Clone or download this repository to your local machine.
2. Open the `morse_code.py` file in a Python-compatible IDE or text editor.

### Encrypting a Message

To encrypt a text message, use the `encrypt` function. Provide the message as an argument, and the function will return the Morse code representation of the message.

Example:
```python
message = "Hello World"
encrypted_message = encrypt(message.upper())
print(encrypted_message)
```

### Decrypting a Message

To decrypt Morse code back into text, use the `decrypt` function. Provide the Morse code message as an argument, and the function will return the original text message.

Example:
```python
morse_code_message = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
decrypted_message = decrypt(morse_code_message)
print(decrypted_message)
```

## Example Usage

```python
# Import the functions from the morse_code.py module
from morse_code import encrypt, decrypt

# Encrypt a message
message = "Hello Morse Code"
encrypted_message = encrypt(message.upper())
print("Encrypted Message:", encrypted_message)

# Decrypt a message
morse_code_message = ".... . .-.. .-.. --- / -- --- .-. ... . / -.-. --- -.. ."
decrypted_message = decrypt(morse_code_message)
print("Decrypted Message:", decrypted_message)
```