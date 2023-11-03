from booklet import Booklet
import os
import sys

from printer import Printer


def list_files_with_ext_from_dir(dir_name, ext):
    return [file for file in os.listdir(dir_name) if file.endswith('.' + ext)]

def list_filenames_with_ext(dir_name, ext):
    files = list_files_with_ext_from_dir(dir_name, ext)
    files_in_read_order = []
    for file in files:
        #Zapisz sciezke do pliku w tablicy
        files_in_read_order.append(os.path.join(dir_name, file))
    return files_in_read_order

def exit_program():
    print("Exiting the program...")
    sys.exit(0)

def main():
    if len(sys.argv) > 1:
        dir_to_lookup = sys.argv[1]
        if len(sys.argv) > 2:
            ext_to_lookup = sys.argv[2]
        else:
            ext_to_lookup = 'jpg'
    else:
        print(
"""
Provide path to directory, where directories with images are store.
For example, if you have your jpgs in directory /home/user/songs/flute and /home/user/songs/sax
you need to provide /home/user/songs path

I have multiple voices/instruments in my band and I needed a way to quickly go throuth all of them 
so I implemented such solution ;)
"""         )
        exit_program()
    dir_list = []
    directories = []
    for file in os.listdir(dir_to_lookup):
        if '.' not in file: #Not a file. A directory only
            directories.append(file)
    for dir_path in directories:
        dir_list.append(os.path.join(dir_to_lookup, dir_path))

    for p in range(0, len(dir_list)):
        print(".")
        dir_name = dir_list[p]
        files_in_read_order_a = list_filenames_with_ext(dir_name, ext_to_lookup)
        b = Booklet(len(files_in_read_order_a))
        b.assign_images(files_in_read_order_a)
        p = Printer()
        p.save(b, dir_name)
    exit_program()

if __name__ == "__main__":
    main()