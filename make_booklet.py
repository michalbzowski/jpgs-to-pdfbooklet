from booklet import Booklet
import os

from printer import Printer

dir_to_lookup = "C:\\Users\\Monika Bzowska\\IdeaProjects\\band-book-maker-main-kosicelne\\src\\main\\resources\\NUTY_KOSCIELNE"


def list_jpgs_from_dir(dir_name):
    return [file for file in os.listdir(dir_name) if file.endswith('.jpg')]

def list_jpg_names(dir_name):
    jpg_files = list_jpgs_from_dir(dir_name)
    files_in_read_order = []
    for jpg_file in jpg_files:
        #Zapisz sciezke do pliku w tablicy
        files_in_read_order.append(os.path.join(dir_name, jpg_file))
    return files_in_read_order

dir_list = []
for dir_path in os.listdir(dir_to_lookup):
    dir_list.append(os.path.join(dir_to_lookup, dir_path))

for p in range(0, len(dir_list)):
    print(".")
    dir_name = dir_list[p]
    files_in_read_order_a = list_jpg_names(dir_name)
    b = Booklet(len(files_in_read_order_a))
    b.assign_images(files_in_read_order_a)
    p = Printer()
    p.save(b, dir_name)