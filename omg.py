import math
from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import landscape
from reportlab.pdfgen import canvas
import os

dir_to_lookup = "C:\\Users\\Monika Bzowska\\IdeaProjects\\band-book-maker-main-kosicelne\\src\\main\\resources\\NUTY_KOSCIELNE"
empty_page_path = "C:\\Users\\Monika Bzowska\\IdeaProjects\\band-book-maker-main-kosicelne\\src\\main\\resources\\empty_page.jpg"

class Booklet:
    """Booklet representation"""
    images_count = 0
    documents_per_page = 0 #dozwolone 1 albo 2
    booklet_pages_count = 0 #obliczne w konstruktorze
    images_in_booklet = []
    currently_returnet_image = 0
    booklet_sheets_count = 0
    images_count = 0

    def __init__(self, images_count, documents_per_page):
        self.documents_per_page = documents_per_page
        self.booklet_pages_count = math.ceil(images_count / 4) * 4 ## Założenie, że zawsze parzyste
        self.booklet_sheets_count = math.ceil(images_count / 4)
        self.images_count = images_count

    def assign_images(self, images):
        self.images_in_booklet = []
        self.currently_returnet_image = 0
        current_sheet = 1
        i = 1
        current_page = 1
        RIGHT = 1
        LEFT = 0
        edge = -1
        for n in range(0, int(self.booklet_pages_count/2)):
            if n >= len(images): 
                break
            image = images[n]
            if i % 2 == 0:
                edge = LEFT
            else:
                edge = RIGHT
            self.images_in_booklet.append(BookletImage(image, edge, 0, current_page, current_sheet, "A"))
            i = i + 1
            if n == int(self.booklet_pages_count/2) - 1:
                break
            else:
                current_page = current_page + 1
            if i % 2 == 1:
                current_sheet = current_sheet + 1

        for n in range(int(self.booklet_pages_count/2), self.booklet_pages_count):
            if n >= len(images): 
                break
            image = images[n]
            if i % 2 == 0:
                edge = LEFT
            else:
                edge = RIGHT
            self.images_in_booklet.append(BookletImage(image, edge, 0, current_page, current_sheet, "A"))
            if n == self.booklet_pages_count:
                break
            i = i + 1
            current_page = current_page - 1
            if i % 2 == 1:
                current_sheet = current_sheet - 1

    
    def return_next_image(self):
        return_now = self.currently_returnet_image
        self.currently_returnet_image = self.currently_returnet_image + 1
        return self.images_in_booklet[return_now]
    
    def return_images_with_page(self, page_number):
        pages = []
        for image in self.images_in_booklet:
            if image.booklet_page == page_number:
                pages.append(image)
        return pages

class BookletImage:
    """One imge in booklet - so it is one file with coordinates where to place it"""
    path = ""
    edge = 0 #0 is snap to left, 1 is snap to right
    y = 0 #0 is snap to top, 1 is snap to bottom
    booklet_page = 0
    booklet_sheet = 0
    booklet_side = "" #Side A or Side Bs

    def __init__(self, path, edge, y, booklet_page, booklet_sheet, booklet_side):
        self.path = path
        self.edge = edge
        self.y = y
        self.booklet_page = booklet_page
        self.booklet_sheet = booklet_sheet
        self.booklet_side = booklet_side

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

def list_jpgs_from_dir(dir_name):
    return [file for file in os.listdir(dir_name) if file.endswith('.jpg')]

def list_jpg_names(dir_name):
    jpg_files = list_jpgs_from_dir(dir_name)
    files_in_read_order = []
    for jpg_file in jpg_files:
        #Zapisz sciezke do pliku w tablicy
        files_in_read_order.append(os.path.join(dir_name, jpg_file))
    return files_in_read_order

def fill_with_empty_page(count):
    a = []
    for n in range(0, count):
        a.append(empty_page_path)
    return a

dir_list = []
for dir_path in os.listdir(dir_to_lookup):
    dir_list.append(os.path.join(dir_to_lookup, dir_path))

for p in range(0, len(dir_list)):
    print(".")
    dir_name = dir_list[p]
    files_in_read_order_a = list_jpg_names(dir_name)
    b = Booklet(len(files_in_read_order_a), 1)
    b.assign_images(files_in_read_order_a)
    p = Printer()
    p.save(b, dir_name)       
    pass


