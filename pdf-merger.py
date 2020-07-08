import os
import PyPDF2
import re

filepath = input('Enter 1st pdf path - ')
file1 = open(filepath, 'rb')

filepath = input('Enter 2nd pdf path - ')
file2 = open(filepath, 'rb')

reader1 = PyPDF2.PdfFileReader(file1)
reader2 = PyPDF2.PdfFileReader(file2)

writer = PyPDF2.PdfFileWriter()

print('First Pdf has ' + str(reader1.numPages) + ' pages')
print('Second Pdf has ' + str(reader2.numPages) + ' pages')

pageNos = []

print('Enter the order of pages in the format : "Pdf no - Starting Page - Ending Page" \nEnter -1 once you\'re done')

choiceRegex = re.compile(r'(\d) *- *(\d+) *- *(\d+)')

while True:
    choice = input()
    if choice == '-1':
        break
    mo = choiceRegex.findall(choice)
    pageNos.append(mo[0])

for pages in pageNos:
    pdf = int(pages[0])
    start = int(pages[1])
    end = int(pages[2])

    if pdf == 1:
        for pageNum in range(start-1, end):
            page = reader1.getPage(pageNum)
            writer.addPage(page)
    else:
        for pageNum in range(start-1, end):
            page = reader2.getPage(pageNum)
            writer.addPage(page)

outputFile = open('merged.pdf', 'wb')
writer.write(outputFile)

outputFile.close()
file1.close()
file2.close()