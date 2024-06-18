from functools import reduce

#Demonstrating the map function
square = lambda x: x*x
l = [1, 2, 3, 4]
c = map(square, l)
print(list(c))

#Demonstrating the filter function 
greater = lambda x: x>4
a = [1,2, 3, 4, 5, 58, 30]
d = filter(greater, a)
print(list(d))

#Demonstration for reduce
sum = lambda x, y : x+y
a = [1, 2, 3, 4]
d = reduce(sum, a)
print(d)
