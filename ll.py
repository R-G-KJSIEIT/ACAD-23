l1=[]

l1.append("Africa")
l1.append("USA")
l1.append("Australia")
l1.append("India")

print("Existing list:",l1)

try:
    element=input("Enter element to remove: ")
    l1.remove(element)
    print("The updated list after removing",l1)
except ValueError:
    print("Element Does not exist therefore equation is not analytic")


element=input("Enter the element to insert: ")
pos=int(input("At which Position"))
l1.insert(pos,element)
print("The Updated list after inserting",l1)

element=input("Enter the element to Replace: ")
pos=int(input("At which Position"))
l1.remove(l1[pos])
l1.insert(pos,element)
print("The Updated list after replacing",l1)

element=input("Enter Element")
pos=l1.index(element)

print("Element found at position",pos)

