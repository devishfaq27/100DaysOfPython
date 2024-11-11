alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def encrypt_decrypt(orignal_text, shift_amount, encode_decode):
    output = ""
    if encode_decode == "decode":
        shift_amount *= -1
    for latter in orignal_text:
        if latter not in alphabet:
            output += latter
        else:
            shifted_position = alphabet.index(latter) + shift_amount
            shifted_position %= len(alphabet)
            output += alphabet[shifted_position]

    print(output)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to 'encrypt type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt_decrypt(text, shift, direction)

    restart = input("do you want to continue type 'yes' or 'no':  ")
    if restart == "no":
        should_continue = False
        print("Good bye")
    elif restart == "yes":
        should_continue = True
    else:
        print("Wrong Output")






















# def encrypt(orignal_text, shifted_amount):
#     ciser_text = ""
#     for latter in orignal_text:
#         shifted_position = alphabet.index(latter) + shifted_amount
#         shifted_position %= len(alphabet)
#         ciser_text += alphabet[shifted_position]
#     print(ciser_text)
#
# encrypt(text, shift)



# def decode(orignal_text, shift_amount):
#     output_text = ""
#     for latter in orignal_text:
#         shifted_position = alphabet.index(latter) - shift_amount
#         output_text += alphabet[shifted_position]
#         print(output_text)
#
# # decode(text, shift)


