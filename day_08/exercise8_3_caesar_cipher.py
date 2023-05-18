alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    encripted_message = []
    # Taking each letter in the provided text and checking it with the position of the same letter in the alphabet
    for letter in plain_text:
        letter_index = alphabet.index(letter)
        new_position = letter_index + shift_amount
        
        # Checking if the length of the new position is inferior to the length of the alphabet list plus shift. If so, the new_position is part of the main length of the list.
        if new_position < (len(alphabet) - shift_amount):
            new_letter = alphabet[new_position]
            encripted_message.append(new_letter)

        # Checking if the length of the new_position is superior or equal to the length of the alphabet list plus shift. If so, the new_position is part of the main length of the list.
        if new_position >= (len(alphabet) - shift_amount):
            new_letter_2 = alphabet[new_position - len(alphabet)]
            encripted_message.append(new_letter_2)
    print(f"The encoded text is: {str(encripted_message)}.")


def decrypt(encripted_message, shift_amount):
    decoded_message = []
    # Taking each letter in the provided encripted message and checking it with the position of the same letter in the alphabet
    for letter in encripted_message:
        letter_index = alphabet.index(letter)
        new_position = letter_index - shift_amount
        
        if new_position < (len(alphabet) - shift_amount):
            new_letter = alphabet[new_position]
            decoded_message.append(new_letter)
            
        if new_position >= (len(alphabet) - shift_amount):
            new_letter_2 = alphabet[new_position - len(alphabet)]
            decoded_message.append(new_letter_2)
    print(f"The decoded text is: {str(decoded_message)}.")


if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
else:
    decrypt(encripted_message=text, shift_amount=shift)
