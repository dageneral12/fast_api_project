import os

print(os.getcwd())

import PyPDF2 as pdf

file = open('sample.pdf', 'rb')
pdf_reader = pdf.PdfFileReader(file)

#help(pdf_reader)

#pdf_reader.getIsEncrypted()
#pdf_reader.GetNumPages()


#extracting p1 

page1 = pdf_reader.getPage(0)

#Extracts data from a page 
some_text = page1.extractText()

print(some_text)
print(type(some_text))

doc_info = pdf_reader.getDocumentInfo()
print(doc_info)


#page2 = pdf_reader.GetPage(1)

#page2.extractText()

#Append, write or merge PDF files 

#Appends pages to the file: 


#pdf_writer = pdf.PdfFileWriter()

#pdf_writer.addPage(page1)
#pdf_writer.addPage(page2)

#Reverse the order of the pages to reverse the order in which they appear in the doc


#output = open('Pages.pdf', 'wb')

#pdf_writer.write(output)
