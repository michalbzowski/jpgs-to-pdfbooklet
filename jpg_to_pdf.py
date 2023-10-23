from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import landscape
from reportlab.pdfgen import canvas
import os
 

# Ścieżka do katalogu z plikami JPG
dir_to_lookup = "C:\\Users\\Monika Bzowska\\IdeaProjects\\band-book-maker-main-kosicelne\\src\\main\\resources\\NUTY_KOSCIELNE"
empty_page_path = "C:\\Users\\Monika Bzowska\\IdeaProjects\\band-book-maker-main-kosicelne\\src\\main\\resources\\empty_page.jpg"
# Nazwa pliku PDF wynikowego
output_pdf = "wyjściowy.pdf"

# Otwórz plik PDF wynikowy
c = canvas.Canvas(output_pdf, pagesize=A4 )

wi = A4[0]/2
hi = A4[1]/2
dir_list = []
for dir_path in os.listdir(dir_to_lookup):
    dir_list.append(os.path.join(dir_to_lookup, dir_path))

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


empty_page = False
for p in range(0, len(dir_list), 2):
    # Pobierz listę plików JPG w katalogu
    print(".")
    dir_name_a = dir_list[p]

    if p + 1 >= len(dir_list):
        empty_page = True
    else:
        empty_page = False
        dir_name_b = dir_list[p + 1]


    # Dla każdego pliku JPG w katalogu
    files_in_read_order_a = list_jpg_names(dir_name_a)
    if empty_page:
        files_in_read_order_b = fill_with_empty_page(len(files_in_read_order_a))
    else:
        files_in_read_order_b = list_jpg_names(dir_name_b)
        
    page_count = len(files_in_read_order_a)
    if page_count != len(files_in_read_order_b):
        raise Exception("Page count must be the same!")
    
    if page_count % 2 != 0:
        page_count = page_count + 1
    
    for n in range(0, 1 + int(page_count/2)):
        print(".", end = ' ')
        right_path_a = files_in_read_order_a[n]
        if page_count - n >= len(files_in_read_order_a):
            left_path_a = empty_page_path
        else:
            left_path_a = files_in_read_order_a[page_count - n]

        right_path_b = files_in_read_order_b[n]
        if page_count - n >= len(files_in_read_order_b):
            left_path_b = empty_page_path
        else:
            left_path_b = files_in_read_order_b[page_count - n]

        # Dodaj stronę do pliku PDF
        if n % 2 == 0:
            y = hi
            c.drawImage(left_path_a, 0, y, wi, hi, preserveAspectRatio=True)
            c.drawImage(right_path_a, wi, y, wi, hi, preserveAspectRatio=True)
            c.line(0, y, wi, hi)
            y = 0
            c.drawImage(left_path_b, 0, y, wi, hi, preserveAspectRatio=True)
            c.drawImage(right_path_b, wi, y, wi, hi, preserveAspectRatio=True)
        else:
            y = hi
            c.drawImage(right_path_a, 0, y, wi, hi, preserveAspectRatio=True)
            c.drawImage(left_path_a, wi, y, wi, hi, preserveAspectRatio=True)
            y = 0
            c.drawImage(right_path_b, 0, y, wi, hi, preserveAspectRatio=True)
            c.drawImage(left_path_b, wi, y, wi, hi, preserveAspectRatio=True)
    
        c.showPage()

# Zapisz plik PDF
c.save()

print(f"Plik PDF {output_pdf} został utworzony z plików JPG.")




