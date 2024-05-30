nnum = int(input("Enter the number you want to check:"))

for i in range(2, nnum):
    if(nnum%i == 0):
        print("Not prime")
        break
else:
    print("This is prime number")