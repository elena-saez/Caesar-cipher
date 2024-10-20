from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(txt, sft, dir):

    new_text = ""
    if sft > 26:
        sft = sft % 26
    for char in txt:
        if char in alphabet:
            i = alphabet.index(char)
            if dir == "encode":
                new_i = i + sft
            elif dir == "decode":
                new_i = i - sft
            new_text += alphabet[new_i]
        else:
            new_text += char

    print(f"The {dir}d text is {new_text}")


restart = "yes"

while restart == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    restart = input("Do you want to restart the cipher program? Type yes or no\n").lower()


