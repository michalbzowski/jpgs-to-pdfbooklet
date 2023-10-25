from booklet import Booklet
from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import landscape
from reportlab.pdfgen import canvas

class Printer:
    "Class for take preapared Booklet implementation and write it to PDF file"

    def save(self, booklet: Booklet, some_name):
        wi = A4[0]/2
        hi = A4[1]/2
        # Otwórz plik PDF wynikowy
        output_pdf = some_name +"_wyjściowy.pdf"
        c = canvas.Canvas(output_pdf, pagesize=A4)
        max_page_number = -9999
        for booklet_image in booklet.images_in_booklet:
            if booklet_image.booklet_page > max_page_number:
                max_page_number = booklet_image.booklet_page

        for n in range(1, max_page_number + 1):
            pages = booklet.return_images_with_page(n)
            if len(pages) > 0:
                y = hi
                img = pages[0]
                c.drawImage(img.path, wi if img.edge == 1 else 0, y, wi, hi, preserveAspectRatio=True)
            if len(pages) > 1:
                y = hi

                img = pages[1]
                c.drawImage(img.path, wi if img.edge == 1 else 0, y, wi, hi, preserveAspectRatio=True)
            c.showPage()
        
        c.save()
        print(f"Plik PDF {output_pdf} został utworzony z plików JPG.")