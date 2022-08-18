import caesar_cypher_art as art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

def caesar(text, shift, direction):

    result_text = ""

    while direction != 'encode' and direction != 'decode':
        direction = input("Please, enter 'encode' to encrypt or 'decode' to decrypt the message:\n").lower()

    if direction == 'encode':
        encode = True
    if direction == 'decode':
        encode = False

    for char in range(0, len(text)):
        if text[char] in alphabet:
            if encode:
                shifted_index = alphabet.index(text[char]) + shift
                if shifted_index > len(alphabet) - 1:
                    shifted_index -= len(alphabet)
                result_text += alphabet[shifted_index]
            else:
                shifted_index = alphabet.index(text[char]) - shift
                if shifted_index < 0:
                    shifted_index += len(alphabet)
                result_text += alphabet[shifted_index]
        else:
            result_text += text[char]

    if encode:
        print(f"The encrypted text is: '{result_text}'")
    else:
        print(f"The decrypted text is: '{result_text}'")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye!")
