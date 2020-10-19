import zipfile


file = open('new_fil2.txt', 'w+')
file.write('file number 1')
file.close()

file = open('new_file.txt', 'w+')
file.write('file number 2')
file.close()
# Creating files to work with

comp_file = zipfile.ZipFile('comp_folder.zip', 'w')
# Create zip file in write mode.

comp_file.write('new_file.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('new_fil2.txt', compress_type=zipfile.ZIP_DEFLATED)
# Individually adding files to the zip

comp_file.close()
# Zip it.

zip_obj = zipfile.ZipFile('comp_folder.zip', 'r')
# open file

zip_obj.extractall('extracted_content')
# folder name once extracted.

