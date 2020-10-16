import random

class GuessingGame():
    def __init__(self):
        self.ran_choice = random.randint(1,3)

    def reset_random(self):
        print('Restting Random Number')
        self.ran_choice = random.randint(1,10)

    def guess(self):

        user_guess = int(input('Please enter a guess number: '))

        if user_guess == self.ran_choice:
            print(f'Well done Mane, the answer was {self.ran_choice}, damn you smart')
        else:
            if user_guess < self.ran_choice:
                print('Wrong mofo, guess higher')
                self.guess()
            else:
                print('Nah, guess lower')
                self.guess()

go = GuessingGame()

go.guess()