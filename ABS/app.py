Using ```os```, will give you the OS specific version of the filepath creation.

import os

filepath = os.path.join('folder1', 'folder2', 'folder3', 'test.png')

print(filepath)