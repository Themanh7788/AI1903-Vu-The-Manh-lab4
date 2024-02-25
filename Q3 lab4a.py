#1.Seek the beginning of the File
with open('text.txt', 'w') as file:
    file.write("My first lines\nMy second lines")
#2.Seeking the end of file
with open('text.txt', 'a') as file:
    file.write("\nThis content is added to the end of the file")
#3.Seek from the current position
file.seek(0, os.SEEK_CUR)
print(file.tell())
#4.Seek backward with negative Offset
file.seek(-15, os.SEEK_CUR)
print(file.tell())
#5.Use tell() Function to get file handle position
print(file.tell())
