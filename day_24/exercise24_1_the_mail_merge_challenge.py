# Exercise 24.1 The mail merge Challenge

# Instructions
# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



# Get the letter text from the string_letter document and add it into a list
letter = open("day_24/Input/Letters/starting_letter.txt", "r")
letter_list = letter.readlines()

# Get each guest from the invited_names document and add them into a list
invite = open("day_24/Input/Names/invited_names.txt", "r")
invite_list = invite.readlines()

for guest in invite_list:
    # Take out all the spaces from the beggining and the end of the title.
    stripped_guest = guest.strip()
    new_start = letter_list[0].replace("[name]", stripped_guest)
    
    # Generate the letter content as the rest of the code except title.
    letter_content = letter_list[1:]
    clear_letter = "".join(letter_content)
    
    # Generate the name of each document.
    document_name = "day_24/Output/ReadyToSend/letter_for_" + stripped_guest + ".txt"
    
    # Generate the new letters.
    with open(document_name, "w") as new_letter:
        new_letter.write(str(new_start) + "\n" + str(clear_letter)[1:])
