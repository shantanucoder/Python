'''
factorial(n) = n * factorial(n-1)
factoria(4) = 4 X 3 X 2 X 1
factorial(3) = 3 X 2 X 1
factorial(2) = 2 X 1
factorial(1) = 1
factorial(0) = 1 (By definition)
'''

def factorial(n):
#base condition 
    if(n==0 or n==1):
        return 1
    return n * factorial(n-1)

a = factorial(3)
print(a)