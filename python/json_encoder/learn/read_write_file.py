""" Reading lines from a text file"""

with open('test.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # Strip removes leading/trailing whitespace and newlines

# Writing to a text file
with open('test.txt', 'w', encoding='utf-8') as file:
    file.write('This is a line of text.\n')
    file.write('Another line of text.\n')
