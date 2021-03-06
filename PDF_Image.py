import PyPDF2
from wand.image import Image
import io


def pdf_page_to_png(src_pdf, pagenum = 0, resolution = 72):
    """
    Returns specified PDF page as wand.image.Image png.
    :param PyPDF2.PdfFileReader src_pdf: PDF from which to take pages.
    :param int pagenum: Page number to take.
    :param int resolution: Resolution for resulting png in DPI.
    """
    dst_pdf = PyPDF2.PdfFileWriter()
    dst_pdf.addPage(src_pdf.getPage(pagenum))

    pdf_bytes = io.BytesIO()
    dst_pdf.write(pdf_bytes)
    pdf_bytes.seek(0)

    img = Image(file = pdf_bytes, resolution = resolution)
    img.convert("png")

    return img


def Pdf_Parse():
    src_filename = "Files/slide.pdf"
    file = open(src_filename,'rb')
    src_pdf = PyPDF2.PdfFileReader(file)

    # What follows is a lookup table of page numbers within sample_log.pdf and the corresponding filenames.
    npages =src_pdf.getNumPages()

    for i in range(0,npages):
        big_filename = "Pdf_Images/" + "slide_" + str(i) + ".png"
        # small_filename = "Pdf_Images/" + page["filename"] + "_small" + ".png"

        img = pdf_page_to_png(src_pdf, pagenum = i, resolution = 300)
        img.save(filename = big_filename)

        # Ensmallen
        # img.transform("", "200")
        # img.save(filename = small_filename)


Pdf_Parse()
