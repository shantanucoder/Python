

# Q6

oxford = {
    "Lakdi": "Wood",
    "Kurshi": "Chair",
    "Chaku": "Knife"
    }
key = input("Enter the key:-\n")
if(oxford.get(key)== None):
    print("Value you are looking for is not found")
else: 
    print("The value corresponding to your key is:-", oxford.get(key))

