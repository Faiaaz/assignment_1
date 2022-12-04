#Fahim Faiaz

print("enter size of list: ")
n = int(input())
lst = []
for i in range(0, n):
    item = int(input())
    lst.append(item)
print("current list: ", lst)
print()
print("enter number to be deleted: ")
m = int(input())

lst2 = []
for i in range(0, n):
    if lst[i] is not m:
        lst2.append(lst[i])

print(lst2)