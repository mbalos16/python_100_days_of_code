## Assestment: Write a text-based Python program to convert Strings into Morse Code.

# Imports
import ascii_logo_text
import morse_alphabet
import morse_explanation
INVERSE_MORSE_ALPHABET = {value:key for key, value in morse_alphabet.CODE.items()}

# Function encode
def encode_to_morse(text_to_encode):
    text_to_encode = text_to_encode.upper()
    morse_code = ""
    not_printable = ""

    for letter in text_to_encode:
        if letter == " ":
            # add 7 times after each world
            morse_code += "       " 
        elif letter in morse_alphabet.CODE:
            morse_code += morse_alphabet.CODE[letter]
            # add 3 times after each letter 
            morse_code += "   " 
        else:
            not_printable += letter + " "
    return not_printable, morse_code


# Function decode
def decode_from_morse(text_to_decode):
    decoded_text = ""
    not_printable = ""
    for word in text_to_decode.split("       "):
        for letter in word.split("   "):
            if letter in INVERSE_MORSE_ALPHABET:
                decoded_text += INVERSE_MORSE_ALPHABET[letter]
            else:
                not_printable += letter + "   "
        decoded_text += " "
    decoded_text = decoded_text[0:-1].capitalize()
    return not_printable, decoded_text


# Main program
def run_program():
    # Print the ascii logo
    print(ascii_logo_text.logo)
    # Condition to start the loop
    still_continue = "yes"

    while still_continue == "yes":
        # Inputs 
        encode_decode = (input("\n\nWhat would you like to do (options: encode / decode / explanation): ")).lower()


        # Encode
        if encode_decode == "encode":
            text_to_convert = (input(f"Write the text you would like to encode: "))

            #Call tht encode function
            not_printable, morse_code = encode_to_morse(text_to_encode = text_to_convert)

            # Imposible to encode characters
            if len(not_printable) > 1:
                print(f'🥴 Sorry, this character "{not_printable}", cannot be encoded.\nPlease reconsider your message avoiding other characters but space, commas and letters.\n------------------------------------------------\n')
            
            # Encode result
            print("\n---------------- 🔮 ----------------")
            print(f"Your text in Morse code is:\n\n{morse_code}\n\n")


        # Decode
        elif encode_decode == "decode":
            text_to_convert = (input(f"Write the text you would like to decode: ")).upper()

            #Call the decode function
            not_printable, morse_code = decode_from_morse(text_to_decode = text_to_convert)

            # Imposible to decode characters
            if len(not_printable) > 1:
                print(f'🥴 Sorry, this character "{not_printable}", cannot be decoded.\nPlease reconsider your message avoiding other characters but space, commas and letters.\n------------------------------------------------\n')
            
            # Encode result
            print("\n---------------- 🔮 ----------------")
            print(f"Your decoded text from Morse is:\n\n{morse_code}\n\n")


        # Program explanation
        elif encode_decode == "explanation":
            print(morse_explanation.text)


        # Invalid input for encode_decode
        else:
            print("\n---------------- 🚧 ----------------")
            print(f" '{encode_decode}' is not a valid option for this program. \n\
                Please try one of the valid options: encode / decode / explanation")
        still_continue = (input("Would you like to do anything else? (answer: yes / no): "))


    # Ask for feedback
    print("\n---------------- 📬 ----------------")
    print("I would love to improve this program.\nDrop me an email at: mariabalos16@gmail.com if you have any feedback 🤗.")


if __name__ == "__main__":
    run_program()