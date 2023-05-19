# Exercise 8.3 - Caesar_cipher
import art_exercise8_3_caesar_cipher

print(art_exercise8_3_caesar_cipher.logo)
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
    message = ""
    # Taking each letter in the provided text and checking it with the position of the same letter in the alphabet
    for letter in text_parameter:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            if direction_parameter == "encode":
                new_position = letter_index + shift_paramether
                # Checking if the length of the new position is inferior to the length of the alphabet list plus shift. If so, the new_position is part of the main length of the list.
                if new_position < (len(alphabet) - shift_paramether):
                    new_letter = alphabet[new_position]
                    message += new_letter

                # Checking if the length of the new_position is superior or equal to the length of the alphabet list plus shift. If so, the new_position is part of the main length of the list.
                if new_position >= (len(alphabet) - shift_paramether):
                    new_letter_2 = alphabet[new_position - len(alphabet)]
                    message += new_letter_2

            elif direction_parameter == "decode":
                new_position = letter_index - shift_paramether
                if new_position < (len(alphabet) - shift_paramether):
                    new_letter = alphabet[new_position]
                    message += new_letter

                if new_position >= (len(alphabet) - shift_paramether):
                    new_letter_2 = alphabet[new_position - len(alphabet)]
                    message += new_letter_2
        else:
            message += str(letter)
            print(letter)
    print(f"The {direction_parameter}d text is: {message}.")


caesar(shift_paramether=shift, direction_parameter=direction, text_parameter=text)

restart = input("Type 'yes'if you want to go again. Otherwise type 'no'.").lower
if restart == "yes":
    caesar(shift_paramether=shift, direction_parameter=direction, text_parameter=text)
else:
    print("Goodbye!")
