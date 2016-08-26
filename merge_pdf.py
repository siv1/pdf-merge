from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger


def merge_title(title_pdf, body_pdf):
    """
    Merge title page and user guide body.
    """
    merger = PdfFileMerger()
    pdfs = [title_pdf, body_pdf]
    for f in pdfs:
        merger.append(open(f, 'rb'))

    merger.write(open('combined.pdf', 'wb'))

title_pdf = 'title.pdf'
body_pdf = 'manRev1.1.pdf'

merge_title(title_pdf, body_pdf)
