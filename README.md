Have a pdf file saved in the same folder as the source-code.py before executing the file.
Name the pdf sample.pdf. After executing the program, a copy of the same pdf is generated with a password provided as the input and saved as protected.pdf. 

Here's a step-by-step explanation:

Importing Required Modules:

PdfWriter and PdfReader are imported from PyPDF2 to handle PDF reading and writing.
getpass is imported to securely prompt the user for a password.
Creating PdfWriter Object:

pdfwriter = PdfWriter() initializes a new PdfWriter object.
Reading the Existing PDF:

pdf = PdfReader("sample.pdf") reads the PDF file named "sample.pdf" into a PdfReader object.
Adding Pages to PdfWriter:

A loop iterates over all pages in the pdf object (len(pdf.pages) gives the number of pages), adding each page to the pdfwriter object with pdfwriter.add_page(pdf.pages[page_num]).
Getting Password from User:

passw = getpass.getpass(prompt='Enter Password: ') prompts the user to enter a password without echoing it on the screen.
Encrypting the PDF:

pdfwriter.encrypt(passw) encrypts the PDF with the entered password.
Writing the Encrypted PDF to a File:

The new encrypted PDF is saved to a file named "ho.pdf" using a with open('protected.pdf', 'wb') as f block. This ensures that the file is properly closed after writing.
This script effectively creates a password-protected version of the input PDF file. Make sure you have PyPDF2 installed in your environment; if not, you can install it using pip install pypdf2.
