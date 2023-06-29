l1 = []
for i in range(5):
    num = int(input("Enter a number: "))
    l1.append(num)
print("List of numbers:", l1)
#sum of elements
print("sum:",sum(l1))
#smalllest number
print("min:",min(l1))
#largest numbers
print("max:",max(l1))
#ascending order
l1.sort()
print("sort ascending: ",l1)
#descending order
l1.sort(reverse=True)
print("sort descending:",l1)
#converting list into tuple
t1=tuple(l1)
print("list: ",l1)
print("tuple: ",t1)
#delete the list
del l1
print(l1)
