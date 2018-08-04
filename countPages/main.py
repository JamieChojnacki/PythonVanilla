import PyPDF2 as pypdf
import os

""" lets get en empty list and a working directory """
pdfFiles = []
os.chdir('/Users/James/Desktop/Python Docs')


for filename in os.listdir():
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

pdfFiles.sort(key=str.lower)

pdfWriter = pypdf.PdfFileWriter()


""" open every single pdf """

for filename in pdfFiles:
    with open(filename, 'rb') as pdfFileObj:
        pdfReader = pypdf.PdfFileReader(pdfFileObj)

        """ count page numbers """
        for pageNum in range(1, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)

os.chdir('/Users/James/Desktop/Code/Python/advanced/countPages')
with open('pages.txt', 'wb') as result:
    pdfWriter.write(result)

# TODO
""" delete junk """
