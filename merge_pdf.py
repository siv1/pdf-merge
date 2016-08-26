from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger


def merge_pdfs(first_pdf, second_pdf):
    """
    Merge title page and user guide body.
    At the moment, only have functionality for
    2 PDF files, intend to expand this
    """
    merger = PdfFileMerger()
    pdfs = [first_pdf, second_pdf]
    for f in pdfs:
        merger.append(open(f, 'rb'))

    merger.write(open('combined.pdf', 'wb'))

first_pdf = 'your_pdf_name.pdf'
second_pdf = 'your_pdf_name.pdf'

merge_title(title_pdf, body_pdf)
