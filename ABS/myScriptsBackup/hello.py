from sys import argv

script, first, second = argv

print("This has to be in the same folder as the command files??")
print(first + " needed a $* sign to work")
print(second + " needed a $* sign to work")

# So in order to work, i had to make the .command file
# executable, then import sys.argv and pass it arguments
# via terminal. Spotlight doesn't work. $ and not % like windows
# to forward arguments, see below for command file.

    # #!/usr/bin/env bash

    # python3 /Users/calvin/myScripts/hello.py $*