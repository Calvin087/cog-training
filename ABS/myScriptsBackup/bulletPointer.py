#! python3
# bulltPointer - Adds wiki bullets to the start
# of each line of text on the clipboard.

import sys, pyperclip

clipboard_text = pyperclip.paste()

copied_lines = clipboard_text.split('\n')

for i in range(len(copied_lines)):
    copied_lines[i] = '* ' + copied_lines[i]

clipboard_text = '\n'.join(copied_lines)


pyperclip.copy(clipboard_text)