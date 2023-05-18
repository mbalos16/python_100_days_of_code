# Exercise 8.3 - Caesar_cipher

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


def caesar(shift_paramether, text_parameter, direction_parameter):
    if direction_parameter == "encode":
        encripted_message = []
        # Taking each letter in the provided text and checking it with the position of the same letter in the alphabet
        for letter in text_parameter:
            letter_index = alphabet.index(letter)
            new_position = letter_index + shift_paramether

            # Checking if the length of the new position is inferior to the length of the alphabet list plus shift. If so, the new_position is part of the main length of the list.
            if new_position < (len(alphabet) - shift_paramether):
                new_letter = alphabet[new_position]
                encripted_message.append(new_letter)

            # Checking if the length of the new_position is superior or equal to the length of the alphabet list plus shift. If so, the new_position is part of the main length of the list.
            if new_position >= (len(alphabet) - shift_paramether):
                new_letter_2 = alphabet[new_position - len(alphabet)]
                encripted_message.append(new_letter_2)
        print(f"The encoded text_parameter is: {str(encripted_message)}.")

    if direction_parameter == "decode":
        decoded_message = []
        # Taking each letter in the provided encripted message and checking it with the position of the same letter in the alphabet
        for letter in text_parameter:
            letter_index = alphabet.index(letter)
            new_position = letter_index - shift_paramether

            if new_position < (len(alphabet) - shift_paramether):
                new_letter = alphabet[new_position]
                decoded_message.append(new_letter)
            if new_position >= (len(alphabet) - shift_paramether):
                new_letter_2 = alphabet[new_position - len(alphabet)]
                decoded_message.append(new_letter_2)
        print(f"The decoded text_parameter is: {str(decoded_message)}.")


caesar(shift_paramether=shift, direction_parameter=direction, text_parameter=text)
