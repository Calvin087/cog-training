# Cypher? Sypher?

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

    return ''.join(encrypted_text)
    

def decrypt_it(text, shift):
    alpha = string.ascii_lowercase
    first_half = alpha[:shift] # --> abc
    second_half = alpha[shift:] # --> defghijklmno...
    shifted_alpha = second_half + first_half # --> defghijklmnop...abc
    decrypted_text = list(range(len(text))) # --> [0, 1, 2, 3, 4, 5, 6, 7, 8]

    for i, letter in enumerate(text.lower()):
        
        if letter in alpha:
            index = shifted_alpha.index(letter) # --> 2, 0, 11
            orig_letter = alpha[index] # --> cal
            decrypted_text[i] = orig_letter
        else:
            decrypted_text[i] = letter

    return ''.join(decrypted_text)

def brute_force(text):
    for n in range(26):
        print(f"Using a shift val of {n}")
        print(decrypt_it(text, n))
        print('\n')

# print(encrypt_it("Cal", 3))
# print(decrypt_it("fdo", 3))
# print(brute_force("fdo"))