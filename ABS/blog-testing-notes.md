<br>

# Working With Files

<br>

On macs, it's easier. You don't need to escape the back slash

```/Users/asd/Documents/python-refresher.md```

You can also use the .join method.

```py

filepath = '/'.join(['folder1', 'folder2', 'folder3'])

print("Users/" + filepath)

```

Using ```os```, will give you the OS specific version of the filepath creation.

This would look different on a Windows I guess.

```py

import os

filepath = os.path.join('folder1', 'folder2', 'folder3', 'test.png')

print(filepath)

```

Getting the full path from where i am right now.
You can basically check if folders exist, get absolute paths, make files and folders and see if a list of files inside a folder etc.

```py

os.path.abspath('../spam.png')
os.path.exits('../spam.png')

```

<br>

# Reading and Writing text files

<br>

```py

hello = open.(filename.txt)
hello.read()
hello.close()

```
opens the file in read mode. Can't edit anything.

Once you open a file you can save the contents to a variable.

```py
hello = open(hello.txt, 'w')
contents = hello.read()
hello.write('writing text to a file')
hello.close()

```

Look up Shelve module, storing lists, and dictionaries to files. They're very similar to key value pairs.

<br>

# Moving Files

<br>

```import shutil```

.copy() / .copytree() / .move() 