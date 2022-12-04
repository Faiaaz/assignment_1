# Fahim Faiaz

lst1 = []

n = int(input("enter number of elements: "))

for i in range(0,n):
    item = int(input())
    lst1.append(item)

for i in reversed(range(n)):
    print(lst1[i], end=" ")