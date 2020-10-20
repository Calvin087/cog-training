import PyPDF2

my_pdf = open('fitness_notes.pdf', 'rb')
# rb is read as binary.

pdf_reader = PyPDF2.PdfFileReader(my_pdf)

# print(pdf_reader.numPages)
# >> 71

page_one_v = pdf_reader.getPage(7)
# reads page 7

page_one_text = page_one_v.extractText()
# takes text from page 7 and prints it

#---------------------- list of pages

# pdf_text = []

# for n in range(pdf_reader.getNumPages()):
#     page = pdf_reader.getPage(n)

#     pdf_text.append(page.extractText())

#----------------------

my_pdf.close()

print(page_one_text)

# ----- Appending pages and Copying. 
# ----- We can't edit text because of all the variable fonts etc that are in the way

my_pdf1 = open('fitness_notes1.pdf', 'rb')

pdf_reader1 = PyPDF2.PdfFileReader(my_pdf1)
first_page = pdf_reader1.getPage(1)
# python indexing 0::-1


pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(first_page)

pdf_output = open('some_new.pdf', 'wb') # or ab to append

pdf_writer.write(pdf_output)

my_pdf1.close()
pdf_output.close()
