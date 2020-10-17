# So i cheated and imported my c cyper from the last exercise.
# I doubt this is the correct way to do it, but it works 
# for smaller strings.


import string
import random

class Encrypt_it():

    def __init__(self, seed):
        random.seed(seed)

        self.seed = seed
        self.encrypted_phrase = ''
        self.true_alpha = list(string.ascii_lowercase)
        self.rand_alpha = random.sample(self.true_alpha, len(self.true_alpha))

    def encryption(self, message):
        output = ''

        for i in range(len(message)):
            output += message[i]
            # so we concate i
            output += random.sample(self.true_alpha, 1)[0]
            # then we concat the first[0] random sample from the alpha list

        self.encrypted_phrase = output[::-1]
        # I've now replaced the attribute above with the reversed output

        # ceasar goes here
        encrypted_phase_two = list(range(len(self.encrypted_phrase)))
        # This is a list from 0 to x based on the letters in self.en phrase.
        # I'm going to use these numbers to loop through the phrase
        # Then i'm going to replace each number with a letter

        for i, letter in enumerate(self.encrypted_phrase.lower()):
            # looping through the reversed string and
            # taking the index and letter = unpacking

            if letter in self.true_alpha:
                # so A is my first letter in the phrase
                # index = 0
                index = self.true_alpha.index(letter)

                # now i want the random alphabet letter 
                # at index 0 also.
                # then replace the num in this list below with a letter
                # from random alpha
                encrypted_phase_two[i] = self.rand_alpha[index]

            else:
                # catching punctuation
                encrypted_phase_two[i] = letter

        # encrypted_phase_two is now a list of letters from 
        # the random alphabet
        # amd we join the list below into a string.

        self.encrypted_phrase = ''.join(encrypted_phase_two)

        return self.encrypted_phrase

    def decryption(self, message, seed):
        
        random.seed(seed)

        # not sure why we're making this again.
        session_rand_alpha = random.sample(self.true_alpha, len(self.true_alpha))

        # going to be using this as a list of numbers 
        # then replace each num with a decrypted letter
        decrypted_message = list(range(len(message)))
        
        for i, letter in enumerate(message.lower()):
            
            if letter in self.true_alpha:
                
                # Opposite of encrypt
                # Basically i'm flipping the order of use of the alphas.
                index = session_rand_alpha.index(letter)

                # Opposite of encrypt, we're finding location
                # of random alpha A eg and putting it back in it's place
                # I guess this all only works because of the SEED being the same.
                decrypted_message[i] = self.true_alpha[index]

            else:
                # Puncuation / spaces
                decrypted_message[i] = letter

        decrypted_message = ''.join(decrypted_message)[::-1]
        
        # !! return this string, from start to end :: in step sizes of 2!!!
        return decrypted_message[::2]

seed = 20

test = Encrypt_it(seed) #20 is the seed?? Gives me a routine shuffle??

print(test.encryption('Calvin is ok but not for long'))
print(test.decryption('kdkpzcfgx ijmcuuf zmacapt zmfwdve indcv koofd epbfrlqghxwe', seed))
