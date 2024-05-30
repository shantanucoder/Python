a = [1,2,3,4,5]

for item in a:
    print(item)
    if(item == 4):
        break
    print("The iteration is for", item)

else:
    print("We are inside the else")
print("We have completed the loop!!")
