import os
from PyPDF2 import PdfMerger

def merge_pdfs(input_dir, output_file):
    pdf_merger = PdfMerger()

    # Pobierz listę plików PDF w katalogu źródłowym
    pdf_files = [file for file in os.listdir(input_dir) if file.endswith(".pdf")]

    if not pdf_files:
        print("Brak plików PDF do połączenia w podanym katalogu.")
        return

    # Sortuj pliki PDF alfabetycznie
    pdf_files.sort()

    try:
        # Dodaj pliki PDF do obiektu PdfMerger
        for pdf_file in pdf_files:
            with open(os.path.join(input_dir, pdf_file), 'rb') as pdf:
                pdf_merger.append(pdf)

        # Zapisz połączone pliki PDF do pliku docelowego
        with open(output_file, "wb") as output:
            pdf_merger.write(output)
        print(f"Pliki PDF zostały połączone i zapisane jako '{output_file}'.")
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisywania pliku PDF: {e}")
    finally:
        pdf_merger.close()

if __name__ == "__main__":
    input_directory = ""
    output_file = ""

    if not os.path.exists(input_directory):
        print("Podany katalog nie istnieje. Sprawdź ścieżkę i spróbuj ponownie.")
    else:
        merge_pdfs(input_directory, output_file)
