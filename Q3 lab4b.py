#1. Write a function in Python to count uppercase characters in a text file.
def count_upper(file_name):
    count = 0
    with open(file_name, 'r') as file:
        line = file.read()
        words = line.split()
        for word in words:
            if 'A' <= word[0] and word[0] <= 'Z':
                count += 1
        return count
counts = count_upper('story.txt')
print(counts)
#2. Write a function in Python to count the words &quot;this&quot; and &quot;these&quot; present in a text file&quot;article.txt&quot;. [Note that the words &quot;this&quot; and &quot;these&quot; are complete words]
def check_words(filename):
    count = 0
    with open(filename, 'r') as file:
        line = file.read()
        words = line.split()
        for word in words:
            if word in ['this','these']:
                count += 1
    return count
print(check_words('article.txt'))
        