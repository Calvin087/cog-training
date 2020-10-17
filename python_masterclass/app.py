# Takes a string
# Add random letters in every other index position
# reverses the string
# shuffles the string
# how to unshuffle with random.seed()?
# decrypt will take the see key to figure things out
# use ceaser cyper method to encrypt more


import string
import random

class Encrypt_it():

    def __init__(self, seed):
        self.seed = seed
        self.phrase = ""

        random.seed(self.seed)
        
        self.alpha = string.ascii_lowercase
        self.shuffle = random.sample(self.alpha, self.seed)
        # empty string for encrypted phrase - done
        # use string and random to create libraries alpha norm and alpha shuffled with random.sample()- done


    def encryption(self, message):
        pass

        # replace every other char with random letter
        # reverse that string
        # use shuffled alpha for ceaser cipher

    def decryption(self, message, seed):
        pass


seed = 20

test = Encrypt_it(seed) #20 is the seed?? Gives me a routine shuffle??
# print(test.alpha)
print(test.shuffle)

# test.encryption('hello')
# test.decryption('UNDO WHAT I DID', 20)