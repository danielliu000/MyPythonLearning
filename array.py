from array import *

arr = array('i', [3, 4, 5])
print(arr)
n = input('Enter the length of your array: ')

for i in range(n):
    x = int(input("Enter next value of your array: "))
    arr.append(x)

print(arr)
