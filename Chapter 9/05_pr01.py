with open("poem_lyrics.txt", "w") as f:
    f.write("shantanu IS HERE !!")


with open("poem_lyrics.txt", "r") as f:
    if("shantanu" in f.read()):
        print("Yes shantanu word is present in the given file")
    else:
        print("No, the word shantanu is not present in the file!!!!")