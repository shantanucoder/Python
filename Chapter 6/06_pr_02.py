#check if the marks of the students are greater than 33 marks and the percentage of 
#marks of each subject is at least 40 


m1 = int(input("Enter the marks of subject 1:"))
m2 = int(input("Enter the marks of subject 2:"))
m3 = int(input("Enter the marks of subject 3:"))

overALL = (m1+m2+m3)/3

if(overALL>=40):
    if(m1>=33 and m2>=33 and m3>=33):
     print("You have passed the exam !")
    else:
       print("You have FAILED the exam for one of the subjects")
else:
    print("You have FAILED the exam for not achieving the threshold percentage marks!!")