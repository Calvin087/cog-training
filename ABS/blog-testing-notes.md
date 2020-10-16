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