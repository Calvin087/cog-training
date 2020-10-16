import string


def encrypt_it(text, shift):
    alpha = string.ascii_lowercase
    first_half = alpha[:shift] # --> abc
    second_half = alpha[shift:] # --> defghijklmno...
    shifted_alpha = second_half + first_half # --> defghijklmnop...abc
    encrypted_text = list(range(len(text))) # --> [0, 1, 2, 3, 4, 5, 6, 7, 8]

    for i, letter in enumerate(text.lower()):
        
        if letter in alpha:
            old_index = alpha.index(letter) # --> 3, 0, 21, 4
            new_letter = shifted_alpha[old_index] # --> gdyh
            encrypted_text[i] = new_letter
        else:
            encrypted_text[i] = letter

    return encrypted_text
    
print(encrypt_it("Dave!1212", 3))