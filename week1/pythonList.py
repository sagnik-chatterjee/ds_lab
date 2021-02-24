list1=['abcd',786,2.23,'john',70.2]
tinylist=[123,'john']
#print the list 
print(list1)
#print the first elem of the list1 
print(list1[0])

#print elements of the list starting from 2nd till 3rd 
print(list1[1:3])

#prints elemenets of the list starting from 3rd elem 
print(list1[1:])

#print list 2 times 
print(tinylist*2)

#prints concatenated list 
print(list1+tinylist)


## functions and methods of list 

list2=['physics','chemistry',1997,2000]
list2.append('maths')
print(list2)

del list2[2]##removes the 3rd elem 
print(len(list2))

print(list2.count('physics'))

#to return the last elemnt of the list 
print(list2.pop())

#inserting a item at the specific index 
list2.insert(2,'geography')
print(list2)
# remove the speicifc item 
list2.remove('chemistry')
print(list2)

##reversing the objects of the list 
list2.reverse()
print(list2)











