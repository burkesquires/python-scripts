import PyPDF2
file = input("Name of your pdf file you want to extract a page from: ")
pdfFileObj = open(f'{file}.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pgnumber = input("Which page would you like to extract?: ")
pageObj = pdfReader.getPage(int(pgnumber) - 1)
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(pageObj)
outputfile = input("Name new pdf file: ")
with open(f'{outputfile}.pdf', 'wb') as pdfOutputFile:
    pdfWriter.write(pdfOutputFile)
