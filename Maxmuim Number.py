# Creating an empty list
list1 = []
 
# asking number of elements to put in list
a= int(input("Enter number: "))
b= int(input("Enter number: "))
c= int(input("Enter number: "))
 
list1.append(a)
list1.append(b)
list1.append(c)
if (a==b==c):
     print("They are equal")
else:
# Printing maximum element
    print("Largest element is:", max(list1))