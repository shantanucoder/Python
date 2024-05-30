with open('file.txt', 'r') as f:
    text = f.read()



with open('file_copy.txt','w') as f:
    f.write(text)