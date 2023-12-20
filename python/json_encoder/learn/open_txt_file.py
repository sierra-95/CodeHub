"""Opening a text file for reading"""
#open(filename,mode,encoding=None)
with open('sample.txt', 'r', encoding='utf-8') as file:
    #file.read(size)
    #size is optional but is provided in bytes
    content = file.read(100)
    print(content)


