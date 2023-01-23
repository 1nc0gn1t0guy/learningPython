import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)


def cesar(plain_text, shift_amount, direction_chosen):
    end_text = ""
    
    for letter in plain_text:

        if letter in alphabet:
            position = alphabet.index(letter)

            if direction_chosen == "encode":
                new_position = position + shift_amount
                if new_position > 25:
                    new_position = new_position - 26      
            else:
                new_position = position - shift_amount
                if new_position < 0:
                    new_position = new_position + 26
                
            end_text += alphabet[new_position]
        else:
            end_text += letter
            
    print(f"Here's the {direction}d result: {end_text}")


running = True



while running:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    cesar(plain_text=text, shift_amount=shift, direction_chosen=direction)

    if input("Do you want to continue? (yes/no) \n") == "no":
        running = False

