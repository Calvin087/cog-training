import os
import csv
import PyPDF2
import re

spy_doc = open('download_link.csv', encoding='utf-8')

csv_reader = csv.reader(spy_doc)
csv_lines = list(csv_reader)

code = []

for row in csv_lines:
    code.append(row[2])


print(''.join(code))
# >> prints code correctly!

# >> https://drive.google.com/file/d/14oSxiKv35enpyyr81dDqEhk

#Contact_Email_Information.pdf

spy_pdf = open('Contact_Email_Information.pdf', 'rb')

read_spy_pdf = PyPDF2.PdfFileReader(spy_pdf)

extracted_pages = []

for n in range(read_spy_pdf.getNumPages()):
    
    page = read_spy_pdf.getPage(n)

    extracted_pages.append(page.extractText())


# print(extracted_pages)
# >> prints all pages correctly!

# --- Regex Time


for page in range(len(extracted_pages)):

    pattern = r'[\w]+@[\w.]+'
    match = re.search(pattern, extracted_pages[page])
    
    if match != None:
        print(match.group())

# WOOOOOOOOOO!