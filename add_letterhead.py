# A small script to add your letter head to a PDF file.

from PyPDF2 import PdfFileWriter, PdfFileReader

# Open original document
output = PdfFileWriter()
input1 = PdfFileReader(open("orig_doc.pdf", "rb"))
# Add letterhead
for i in range(0, 5):
    mod_page = input1.getPage(i)
    watermark = PdfFileReader(open("letterhead_name.pdf", "rb"))
    mod_page.mergePage(watermark.getPage(0))
    output.addPage(mod_page)

outputStream = file("doc_with_letterhead.pdf", "wb")
output.write(outputStream)
