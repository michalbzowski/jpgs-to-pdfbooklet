import os
import shutil

def copy_files_with_name(src_dir, dest_dir, target_file_name):
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file == target_file_name:
                src_file_path = os.path.join(root, file)
                dest_file_name = target_file_name
                dest_file_path = os.path.join(dest_dir, dest_file_name)
                index = 1

                # Sprawdź, czy plik o danej nazwie już istnieje w katalogu docelowym
                while os.path.exists(dest_file_path):
                    base_name, extension = os.path.splitext(target_file_name)
                    dest_file_name = f"{base_name}_{index}{extension}"
                    dest_file_path = os.path.join(dest_dir, dest_file_name)
                    index += 1

                shutil.copy2(src_file_path, dest_file_path)
                print(f"Skopiowano plik {src_file_path} do {dest_file_path}")


if __name__ == "__main__":
    src_directory = ""
    dest_directory = ""
    target_file_name = "28.pdf"

    if not os.path.exists(src_directory) or not os.path.exists(dest_directory):
        print("Podana ścieżka nie istnieje. Sprawdź ścieżki i spróbuj ponownie.")
    else:
        copy_files_with_name(src_directory, dest_directory, target_file_name)
