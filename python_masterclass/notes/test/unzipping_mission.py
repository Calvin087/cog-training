import os
import shutil
import zipfile
import re

# shutil.unpack_archive('unzip_me_for_instructions.zip', 'unpacked_mission', 'zip')

# os.chdir('test/unpacked_mission')
# print(os.getcwd())
# print(os.listdir())

# f = open('Instructions.txt', 'r')
# lines = f.readlines()

test_phrase = 'https://drive.google.com/open?id=1tWJBFrSQL06qTZgkohs4t_a5Cu84AheLo'
test_phrase2 = 'https://docs.google.com/document/d/Q-DcxM17nJm_El0aGsNnY7FajaogRviwja/edit'

patten_to_find = r'https://[-?/_=.\w]+'

# print(re.findall(patten, test_phrase))
# print(re.findall(patten, test_phrase2))
# Make sure the pattern finds the two examples given


def pattern_search(file, pattern=r'https://[-?/_=.\w]+'):

    f = open(file, 'r')
    text = f.read()

    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        return ''

results = []

for folder, sub_folders, files in os.walk('test/unpacked_mission'):
    for f in files:
        full_path = folder+"/"+f

        findings = pattern_search(full_path)

        results.append(findings)


for r in results:

    if r != '':
        print(r.group())