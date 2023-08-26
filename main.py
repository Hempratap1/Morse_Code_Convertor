from art import logo, morse_dict

print(logo)
print("Welcome to Morse Code Converter")
should_continue = True


def encode():
    english_text = input("Paste your text in English here:\n").upper()
    encoded_code = ''
    for text in english_text:
        if text in morse_dict:
            encoded_code += morse_dict[text] + " "
        elif text == " ":
            encoded_code += "|" + " "
        else:
            encoded_code += "?" + " "
    print(encoded_code)


def decode():
    morse_code = input("Paste your Morse code here:\n")
    morse_dict_inv = {v: k for k, v in morse_dict.items()}
    decoded_text = ''
    split_code = morse_code.split()
    for code in split_code:
        if code in morse_dict_inv:
            decoded_text += morse_dict_inv[code]
        elif code == "|":
            decoded_text += " "
        else:
            decoded_text += "?" + " "
    title_text = decoded_text.title()
    print(title_text)


while should_continue:
    user_input = input("Type 'D' if you want to decode into english text or type 'E' if you want to encode "
                       "in Morse code or 'S' if you are done with conversion:\n").upper()
    if user_input == 'D':
        decode()
    elif user_input == 'E':
        encode()
    elif user_input == 'S':
        print("Thank you for using Code Converter")
        should_continue = False
    else:
        print("Invalid input. Please enter 'E' or 'D'.")


