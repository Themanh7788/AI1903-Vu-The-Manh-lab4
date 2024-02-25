#1.Rename a file after checking whether it exists
import os
filename = input("Enter Filename:")
Newname = input("Enter Filename:")
if os.path.exists(filename):
    print("File Exists")
    os.rename(filename,Newname)
else:
    print("File does not exists")
#2. Rename Multiple Files in Python
files_to_rename = ["file1.txt", "file2.jpg", "file3.pdf"]
new_folder_name = "renamed_files"

if not os.path.exists(new_folder_name):
    os.makedirs(new_folder_name)

for file in files_to_rename:
    new_file_name = os.path.join(new_folder_name, file)
    rename_if_exists(file, new_file_name)

folder_path = "source_folder"
files_to_rename_in_folder = ["file1.txt", "file3.pdf"]
new_folder_name = "renamed_files"

if not os.path.exists(new_folder_name):
    os.makedirs(new_folder_name)

for file in os.listdir(folder_path):
    if file in files_to_rename_in_folder:
        file_path = os.path.join(folder_path, file)
        new_file_name = os.path.join(new_folder_name, file)
        rename_if_exists(file_path, new_file_name)


def rename_with_timestamp(file_path):
    timestamp = int(time.time())
    new_file_name = os.path.splitext(file_path)[0] + f"_{timestamp}" + os.path.splitext(file_path)[1]
    rename_if_exists(file_path, new_file_name)

files_to_rename_with_timestamp = ["timestamped_file.txt"]
for file in files_to_rename_with_timestamp:
    file_path = os.path.join("source_folder", file)
    rename_with_timestamp(file_path)


def change_file_extension(file_path, new_extension):
    new_file_name = os.path.splitext(file_path)[0] + new_extension
    rename_if_exists(file_path, new_file_name)

files_to_rename_extension = ["file1.txt", "file2.jpg"]
extensions = {
    "file1.txt": ".pdf",
    "file2.jpg": ".png"
}

for file in files_to_rename_extension:
    file_path = os.path.join("source_folder", file)
    new_extension = extensions[file]
    change_file_extension(file_path, new_extension)