from PyPDF2 import PdfWriter, PdfReader
import getpass

# Create a PdfWriter object
pdfwriter = PdfWriter()

# Read the existing PDF
pdf = PdfReader("sample.pdf")

# Add all pages from the existing PDF to the PdfWriter object
for page_num in range(len(pdf.pages)):
    pdfwriter.add_page(pdf.pages[page_num])

# Prompt the user to enter a password
passw = getpass.getpass(prompt='Enter Password: ')

# Encrypt the PDF with the entered password
pdfwriter.encrypt(passw)

# Save the new encrypted PDF to a file
with open('protected.pdf', 'wb') as f:
    pdfwriter.write(f)
