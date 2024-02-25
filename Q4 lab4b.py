#1
def hash_display(filename):
    with open(filename, 'r') as file:
        line = file.read()
        newline = ''.join(f"{char}#" for char in line)
        print(newline)
hash_display('matter.txt')
#2
def JTOI(filename):
    with open(filename, 'r') as file:
        line = file.read()
        change = line.replace('J','I')
    with open(filename, 'w') as file:
        file.write(change)
    with open(filename, 'r') as file:
        print(file.read())
JTOI('WORDS.TXT')
    
        
        

        