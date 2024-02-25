#Write a function in Python to count and display the total number of words in a text file.
def total_words(filename):
    count = 0 
    with open(filename,  'r')as file:
        for line in file:
            words = line.split()
            count += len(words)
    return count
total = total_words('story.txt')
print(f"Total words are {total}")
#Write a function display_words() in Python to read lines from a text file &quot;story.txt&quot; and displaythose words less than 4 characters.
def display_word(filename):
    count = 0
    short_word = []
    with open(filename, 'r') as file:
        line = file.read()
        lst = line.split()
        for word in lst:
            if len(word) < 4:
                short_word.append(word)
    return (" ".join(short_word))
shortword = display_word('story.txt')
print(shortword)
                
        
                

                    