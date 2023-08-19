# Dictionary representing the morse code chart
MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
}

# Function to encrypt the string according to the morse code chart
def encrypt(message):
    cipher = ""
    for letter in message:
        if letter != " ":
            cipher += MORSE_CODE_DICT[letter] + " "
        else:
            cipher += " "
    return cipher

# Function to decrypt the string from morse to english
def decrypt(message):
    message += " "
    decipher = ""
    citext = ""
    i = 0
    for letter in message:
        if letter != " ":
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += " "
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ""
    return decipher

# Driver function to run the program
def main():
    while True:
        choice = input("Do you want to encrypt or decrypt a message? (encrypt/decrypt/exit): ").lower()

        if choice == "exit":
            print("Exiting the program.")
            break
        elif choice == "encrypt":
            message = input("Enter the message you want to encrypt: ")
            result = encrypt(message.upper())
            print("The encrypted message is:", result)
        elif choice == "decrypt":
            message = input("Enter the message you want to decrypt: ")
            result = decrypt(message)
            print("The decrypted message is:", result)
        else:
            print("Invalid choice. Please enter 'encrypt', 'decrypt', or 'exit'.")

# Executes the main function
if __name__ == "__main__":
    main()
