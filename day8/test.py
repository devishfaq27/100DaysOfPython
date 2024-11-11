alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher_code(original_text, shift_amount, encode_decode):
    output_text = ""
    if encode_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(output_text)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cipher_code(text, shift, direction)

    restart = input("Do you want to continue the game? Type 'yes' or 'no': ").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")
    elif restart == "yes":
        should_continue = True
    else:
        should_continue = False
        print("Invalid input, ending game.")
