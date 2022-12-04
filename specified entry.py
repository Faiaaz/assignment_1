# Fahim Faiaz

lst = [4, 5, 7, 39, 22, 8, 10]

print("select the specific number which precedes the new entry")

n = int(input())

index = lst.index(n)
print("enter new number: ")
new_num = int(input())

lst.insert(index+1, new_num)
print(lst)