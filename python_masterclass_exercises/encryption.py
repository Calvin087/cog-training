# So i cheated and imported my c cyper from the last exercise.
# I doubt this is the correct way to do it, but it works 
# for smaller strings.


import string
import random
import c_cypher

class Encrypt_it():

    def __init__(self, seed):
        self.seed = seed
        self.phrase = ""

        random.seed(self.seed)
        
        self.alpha = string.ascii_lowercase
        self.shuffle = random.sample(self.alpha, self.seed)
        
        # empty string for encrypted phrase - done
        
        # use string and random to create
        # libraries alpha norm and alpha shuffled with random.sample()- done


    def encryption(self, message):

        for i in range(len(message)):
           self.phrase = self.phrase + message[i] + self.shuffle[i]

        self.phrase = self.phrase[::-1]

        return c_cypher.encrypt_it(self.phrase, self.seed)



        # replace every other char with random letter - done
        # reverse that string - done

        # use shuffled alpha for ceaser cipher

    def decryption(self, message, seed):

        self.phrase = c_cypher.decrypt_it(message, seed)

        self.phrase = self.phrase[::-1]

        decrypted_str = ''

        for i in range(len(self.phrase)):
            if i % 2 != 0:
                continue
            else:
                decrypted_str += self.phrase[i]

        return decrypted_str


seed = 20

test = Encrypt_it(seed) #20 is the seed?? Gives me a routine shuffle??

print(test.encryption('Calvin is ok'))
print(test.decryption('aehiu zmecx ohsccpyfpurw', seed))
