# Fahim Faiaz

lst1 = []
lst2 = []

n = int(input("enter number of elements: "))

lst3 = [None] * n

print("enter list 1 elements: ")

for i in range(0,n):
    item = int(input())
    lst1.append(item)

print("enter list 2 elements: ")

for i in range(0,n):
    item2 = int(input())
    lst2.append(item2)

for i in range(0,n):
    lst3[i] = lst1[i] + lst2[i]

print("result: ", lst3)