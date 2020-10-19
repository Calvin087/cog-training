import os
import shutil
import send2trash # allows me to safely delete

file = open('practice.txt', 'w+')

file.write('test line')

file.close()

print("Something Here" + os.getcwd())
# # get current

print(os.listdir())
# # Not working for me

shutil.move('practice.txt', '/Users/calvin/desktop')

shutil.move('/Users/calvin/desktop/practice.txt', os.getcwd())
# This brings the files from where it is to my cwd.

# os.unlink('path')
# delete file

# os.rmdir('path')
# removes empty folder

# shutil.rmtree('path')
# REMOVES EVERTHING FOLDERS AND FILES

send2trash.send2trash('practice.txt')

path_name = '/Users/calvin/Documents/GitHub/cog-training/python_masterclass/notes'

for folder, sub_folders, files in os.walk(path_name):
    print(folder)
    print('\n')

    for sub_folder in sub_folders:
        print(sub_folder)
        
    print('\n')
    
    for sub_folder in sub_folders:
        print(sub_folder)
    
    print('\n')