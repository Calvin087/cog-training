#! python3
# mclip.py - A multi clipboard program.

TEXT = {
    "agree" : "Hell yea bro!!!",
    "busy" : "Not today man, I'm way too busy",
    "upsell" : '''Let's talk about you
paying for my stuff
from now on'''

}


import sys
import pyperclip


# if len(sys.argv) < 2:
#     print("Bro: python mclip.py [keyphrase] - copy phrase text")
#     sys.exit()

# keyphrase = sys.argv[1] # first command line arg is the keyphrase

inputs = input('what.. ')

keyphrase = inputs.lower() # first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print("Text for '" + keyphrase + "' copied to clipboard.")
else:
    print("There is no text for " + keyphrase)

    