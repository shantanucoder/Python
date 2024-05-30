# with open('file.txt', 'r') as f:
#     text = f.read()

# text = text.replace('donkey', '######')

# with open('file.txt','w') as f:
#     f.write(text)





# hi check if python word is present or not :-

with open('file.txt', 'r') as f:
    text = f.read()

p = "python"

if p in text:
    print("hi")
else:
    print("hello")