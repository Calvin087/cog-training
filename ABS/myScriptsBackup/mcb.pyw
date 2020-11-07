#! python3

# mcb.pyw - saves and loads pieces of text to the clipboard.

## Usage:
    # py.exe mcb.pyw save <keyword> - saves clipboard to keyword.
    # py.exe mcb.pyw <keyword> - loads keyword to clipboard
    # py.exe mcb.pyw list - loads all keywords to clipboard

import shelve, pyperclip, sys
import json

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    if sys.argv[1].lower() == 'print':
        for k, v in mcbShelf.items():
            print(k + ": ", v)
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]]) 

mcbShelf.close()
