from art import LOGO

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""

    if cipher_direction == 'decode':
        shift_amount *= (-1)

    for char in start_text:
        if char in ALPHABET:
            current_position = ALPHABET.index(char)
            new_position = (current_position + shift_amount) % len(ALPHABET)
            end_text += ALPHABET[new_position]
        else:
            end_text += char

    print(f"The {cipher_direction}d text is {end_text}")


# Start the Caesar Cypher
print(LOGO)

should_continue = True
while should_continue:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input(
        "Would you like to continue? Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if result == 'no':
        should_continue = False
        print("Thanks for using me. Goodbye!")
