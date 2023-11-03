import os
import pathlib
from pdf2image import convert_from_path, convert_from_bytes

def zgadnijInstrument(pure_path):
    parts = pure_path.parts[-2]
    instrument = str(parts)
    return instrument

def zgadnijUtwor(pure_path):
    parts = pure_path.parts[-1]
    numer = str(parts)[0:2]
    return numer

root = os.getcwd()
root = "C:\\Users\\Monika Bzowska\\Documents\\NUTY_MARSZOWE\STEP_2\\"
target_root = "C:\\Users\\Monika Bzowska\\Documents\\NUTY_MARSZOWE\STEP_2_JPG\\"
for path, subdirs, files in os.walk(root):
    for name in files:
        pure_path = pathlib.PurePath(path, name)
        str_path = str(pure_path)
        if ".pdf" in str_path:
            pages = convert_from_path(str_path, dpi = 300, use_cropbox = True)
            pagesCount = len(pages)
            if pagesCount > 1:
                raise Exception('Za duzo', 'stron') 
            for i in range(pagesCount):
                instrument = zgadnijInstrument(pure_path)
                utwor = zgadnijUtwor(pure_path)
                #step_2 = root + "\\STEP_2\\" + instrument + "\\"
                #write_path = str_path.replace("ZRODLO", "STEP_1")
                write_path = os.path.join(target_root, instrument)
                
                #'C:\\Users\\Monika Bzowska\\Documents\\NUTY_MARSZOWE\\STEP_2\\01_Hymn Polski_PDF_FROM_MUS\\01 hymn - 001 Flet 1.pdf
                #'C:\\Users\\Monika Bzowska\\Documents\\NUTY_MARSZOWE\\STEP_2\\Flet 1\\01.jpg
                if not os.path.exists(write_path):
                    os.makedirs(write_path, mode=0o777)
                pages[i].save(os.path.join(write_path, utwor +".jpg").replace(".pdf", ".jpg"), 'JPEG')