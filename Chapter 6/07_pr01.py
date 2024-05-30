spamWords = ['buy now', 'subscribe now', 'click now', 'click this']

# email = "This is a nice stock you need to click this and buy now stock!!!!"

email = input("Eter your email sentence: ").lower()
spam = False

if('buy now' in email): 
    spam = True

if('click this' in email): 
    spam = True
    
print("Spam is ", spam)


