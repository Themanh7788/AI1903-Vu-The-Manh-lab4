#1.Write to a new file
content = "Done Writing\nThis is new content\n"
with open('f1.txt', 'w') as file:
    file.write(content)
#2. Writing to an existing file
with open('f1.txt', 'a') as file:
    file.write("This is overwritten content\n")
#3.Write a list of lines to a file
lines = ["Name: Emma","Address: 221 Baker Street","City: London"]
with open('f1.txt', 'a') as file:
    file.write('\n'.join(lines))
    