with open('file.txt', 'r') as f:
    text = f.read()



with open('file_copy.txt','r') as f:
    text_copy = f.read()

if text == text_copy:
    print("The file is identical")
else:
    print('The file is not identical bro!')

    